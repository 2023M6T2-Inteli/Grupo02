from tf_transformations import euler_from_quaternion
import json
from build_goals import build_goals


def listener_callback(node, msg):
    node.x = msg.pose.pose.position.x
    node.y = msg.pose.pose.position.y
    rot = msg.pose.pose.orientation
    _, _, node.theta = euler_from_quaternion([rot.x, rot.y, rot.z, rot.w])
    # node.get_logger().info(f"x={node.x:3f}, y={node.y:3f}")


def listener_callback2(node, data):
    # publish the message
    node.logger(json.loads(data.data)["connection"])

    if not node.connected and json.loads(data.data)["connection"] == "true":
        node.connected = True
        node.logger("connected")

    if not node.running:
        data = json.loads(data.data)
        node.logger(str(data))
        if data["edges"] != None and data["nodes"] != None:

            node.running = True
            node.logger("running")
            # (0.0,0.0),*node.point_list[0:node.current_point]]
            node.point_list = build_goals(data)
