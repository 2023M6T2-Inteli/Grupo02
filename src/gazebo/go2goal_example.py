import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry

from publisher_callback import publisher_callback
from listener_callback import listener_callback

from lidar import Lidar


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
        super().__init__('controller')
        self.x, self.y, self.theta = 0.0, 0.0, 0.0
        
        self.vel_msg = Twist()
        self.goal = Point()
        
        self.current_point = 0
        
        self.point_list = goals
        self.return_list = [(0.0, 0.0)]

        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10)
        
        listener_lambda =  lambda msg: listener_callback(self,msg)
        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=listener_lambda,
            qos_profile=10)
        
        self.lidar_ = Lidar(self)

        publisher_lambda =  lambda : publisher_callback(self)
        self.timer = self.create_timer(
            timer_period_sec=0.02,
            callback=publisher_lambda)

                    
    


def main(args=None):
    rclpy.init(args=args)
    controller = TurtleController(goals)
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()