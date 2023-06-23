# Basic ROS 2 program to publish real-time streaming
# video from your built-in webcam
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com

# Import the necessary libraries
import rclpy  # Python Client Library for ROS 2
from rclpy.node import Node  # Handles the creation of nodes
from std_msgs.msg import String  # Standard ROS 2 String message
import json


class ServerCommunicator(Node):

    def logger(self, msg):
        self.get_logger().info(str(msg))

    def timer_callback(self):
        msg = String()

        if not self.connected:
            with open("../../../arquivo.json", 'r') as f:
                file = json.load(f)
                file["connection"] = "true"
                if file["read"] == 0:
                    msg.data = str(file)

        self.publisher_.publish(msg)

    def listener_callback(self, data):
        if not self.connected:
            self.get_logger().info('Connected')
            self.connected = True

            return

    def __init__(self):
        """
        Class constructor to set up the node
        """
        # Initiate the Node class's constructor and give it a name
        super().__init__('connection_starter')

        # Create the publisher. This publisher will publish an Image
        # to the video_frames topic. The queue size is 10 messages.
        self.publisher_ = self.create_publisher(String, 'connection', 10)

        # We will publish a message every 0.1 seconds
        timer_period = 0.1  # seconds
        self.connected = False
        self.running = False
        # Create the timer
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Create the subscriber. This subscriber will receive an json string
        self.subscription = self.create_subscription(
            String,
            'comunication',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning


def main(args=None):

    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create the node
    server_communicator = ServerCommunicator()

    # Spin the node so the callback function is called.
    rclpy.spin(server_communicator)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    server_communicator.destroy_node()

    # Shutdown the ROS client library for Python
    rclpy.shutdown()


if __name__ == '__main__':
    main()
