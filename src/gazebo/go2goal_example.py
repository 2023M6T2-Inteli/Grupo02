import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from math import atan2

from lidar import Lidar

MAX_DIFF = 0.1

goals = [(1.0, 2.0),
         (4.0, 5.0),
         (2.0, 1.0),
         (3.0, 3.0),
         (5.0, 1.0),
         (5.0, 4.0),
         (7.0, 8.0),
         (0.0, 0.0)]

class TurtleController(Node):
    def __init__(self, goals):
        super().__init__('subscriber_node')
        self.x, self.y, self.theta = 0.0, 0.0, 0.0
        
        self.vel_msg = Twist()
        
        self.current_point = 0
        self.point_counter = 1
        self.point_list = goals

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

    # Pegar o goals e seguir o array normal
    def caminho_de_ida(self):

        pass
    
    # Pegar o goals e segue o caminho inverso basedo no "current point"
    def caminho_de_volta(self):

        pass
    
    def chegou_no_ponto(self):
        
        pass
    
    # 
    def update_setpoint(self):
     
        pass

    # Tomador de decisão
    # if's que levam às funções acima
    def publisher_callback(self):
        
        # ele define o goal baseado no array que a gnt passa
        goal = Point()
        goal.x = self.point_list[self.current_point][0]
        goal.y = self.point_list[self.current_point][1]
        
        # calcula a diferença angular entre a frente do robo e o ponto
        inc_x = goal.x - self.x
        inc_y = goal.y - self.y
        angle_to_goal = atan2(inc_y,inc_x)
        
        # try: 
        # decide aqui se há um objeto na frente dele
        # isso vai ser o tomador de decisão
        if self.lidar_.margem_segura() == False:
            raise Exception
        
        # Verifica se o robo chegou no ponto
        # vai passar pras duas funções de movimento
        if (abs(inc_x) < MAX_DIFF and abs(inc_y) < MAX_DIFF):
            self.current_point += self.point_counter
            self.point_counter = 1
            
        # Ajuste do ângulo 
        if abs(angle_to_goal - self.theta) > MAX_DIFF:
            self.vel_msg.linear.x = 0.0
            self.vel_msg.angular.z = 0.3 if (angle_to_goal - self.theta) > 0.0 else -0.3
        # Anda pra frente se o angulo tá certinho
        else:
            self.vel_msg.linear.x = 0.5
            self.vel_msg.angular.z = 0.0
        
        # publica a velocidade
        self.publisher.publish(self.vel_msg)
        
        # except IndexError as err:
        #     self.current_point = 0
        #     self.point_counter = 1
        #     print(err)
            
        # except Exception as error:
        #     self.point_counter = -1
        #     self.current_point += self.point_counter
            
        #     self.vel_msg.linear.x = 0.0
        #     self.vel_msg.angular.z = 0.3
        #     self.publisher.publish(self.vel_msg)
        #     print(error)
        
            



def main(args=None):
    rclpy.init(args=args)
    subscriber_node = TurtleController(goals)
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()