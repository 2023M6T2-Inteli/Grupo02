import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Subscriber(Node):
    def __init__(self):
        super().__init__('controller')
        self.subscription = self.create_subscription(
            msg_type=String,
            topic='/meu_topico',
            qos_profile=10,
            callback=self.listener
        )

    def listener(self, msg):
        print(msg.data)


def main(args=None):
    rclpy.init(args=args)
    controller = Subscriber()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
