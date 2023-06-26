import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Publisher(Node):
    def __init__(self):
        super().__init__('controller')
        self.publisher = self.create_publisher(
            msg_type=String,
            topic='/meu_topico',
            qos_profile=10
        )

        self.timer = self.create_timer(
            timer_period_sec=0.2,
            callback=self.callback
        )

    def callback(self):
        msg = String()
        msg.data = "Oi"

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    controller = Publisher()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
