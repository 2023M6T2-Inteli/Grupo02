from tf_transformations import euler_from_quaternion
def listener_callback(node, msg):
        node.x = msg.pose.pose.position.x
        node.y = msg.pose.pose.position.y
        rot = msg.pose.pose.orientation
        _,_,node.theta = euler_from_quaternion([rot.x,rot.y,rot.z,rot.w])
        # node.get_logger().info(f"x={node.x:3f}, y={node.y:3f}")