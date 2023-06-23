from tf_transformations import euler_from_quaternion
import json
from build_goals import build_goals

def listener_callback(node, msg):
        node.x = msg.pose.pose.position.x
        node.y = msg.pose.pose.position.y
        rot = msg.pose.pose.orientation
        _,_,node.theta = euler_from_quaternion([rot.x,rot.y,rot.z,rot.w])
        # node.get_logger().info(f"x={node.x:3f}, y={node.y:3f}")
def listener_callback2(node, data):
        #publish the message
        if not node.connected:
                node.connected = True
                node.logger("connected")
                


        if not node.running:
                data = json.loads(data.data)
                if ["graph","nodes","edges" ] in data.keys():

                        node.running = True
                        node.logger("running")
                        node.point_list = build_goals(data)#(0.0,0.0),*node.point_list[0:node.current_point]]