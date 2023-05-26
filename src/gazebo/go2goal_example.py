import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from math import atan2

from lidar import Lidar

MAX_DIFF = 0.1

# goals = [(1.0, 2.0),
#          (4.0, 5.0),
#          (2.0, 1.0),
#          (3.0, 3.0),
#          (5.0, 1.0),
#          (5.0, 4.0),
#          (7.0, 8.0),
#          (0.0, 0.0)]

goals = [(2.0, 0.0),
         (2.0, 2.0),
         (0.0, 0.0)]

class TurtleController(Node):
    def __init__(self, goals):
        super().__init__('subscriber_node')
        self.x, self.y, self.theta = 0.0, 0.0, 0.0
        
        self.vel_msg = Twist()
        self.goal = Point()
        
        self.current_point = 0
        self.point_counter = 1
        self.point_list = goals
        self.return_list = [(0.0, 0.0)]

        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10)
        
        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.listener_callback,
            qos_profile=10)
        
        self.lidar_ = Lidar(self)
         
        self.timer = self.create_timer(
            timer_period_sec=0.02,
            callback=self.publisher_callback)

    def listener_callback(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        rot = msg.pose.pose.orientation
        _,_,self.theta = euler_from_quaternion([rot.x,rot.y,rot.z,rot.w])
        # self.get_logger().info(f"x={self.x:3f}, y={self.y:3f}")

    def calculate_goal(self):
        goal = Point()
        goal.x = self.point_list[self.current_point][0]
        goal.y = self.point_list[self.current_point][1]
        return goal

    def calculate_angle_to_goal(self, goal):
        return atan2(goal.y - self.y, goal.x - self.x)

    # Verifica se chegou no ponto (recebe nada, e devolve um bool)
    def check_reached_point(self, inc_x, inc_y):
        return abs(inc_x) < MAX_DIFF and abs(inc_y) < MAX_DIFF

    def adjust_speed(self, angle_to_goal):
        speed = Twist()
        
        
        if abs(angle_to_goal - self.theta) > MAX_DIFF:
            speed.linear.x = 0.0
            speed.angular.z = 0.3 if (angle_to_goal - self.theta) > 0.0 else -0.3
        else:
            speed.linear.x = 0.5
            speed.angular.z = 0.0
        return speed
    

    def handle_index_error(self, error):
        self.current_point = 0
        self.point_list = [(0.0, 0.0)]
        print(error)

    def handle_exception(self, error):
        self.point_list = self.return_list
        print("Point list: ", self.point_list)
        self.current_point = -1
        print(self.current_point)
        self.lidar_.kill_lidar()
        print(error)

    def publisher_callback(self):
        try:
            goal = self.calculate_goal()
            angle_to_goal = self.calculate_angle_to_goal(goal)

            if (self.lidar_.check_safety_margin() == False): 
                self.handle_exception("Não é seguro continuar!")
                    
            if self.check_reached_point(goal.x - self.x, goal.y - self.y):
                
                self.current_point += self.point_counter
                if len(self.return_list) != len(self.point_list) and self.lidar_.permission:
                    self.return_list.insert(0, self.point_list[self.point_counter])
                    print("Return list: ", self.return_list)
                    
                    

            speed = self.adjust_speed(angle_to_goal)
            self.publisher.publish(speed)
                        
        except IndexError:
            self.handle_index_error("List index out of range")
        except Exception as error:
            self.handle_exception(f"Problema: {error}")
        
            



def main(args=None):
    rclpy.init(args=args)
    subscriber_node = TurtleController(goals)
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()