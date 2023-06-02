from auxiliar import calculate_angle_to_goal,calculate_goal,check_lidar_margin,check_reached_point,adjust_speed
from error_handling import handle_exception,handle_index_error
from geometry_msgs.msg import Twist, Point


MAX_DIFF =0.1


def publisher_callback(node):
    try:
        goal = calculate_goal(node)
        angle_to_goal = calculate_angle_to_goal(node,goal)

        if not check_lidar_margin(node):
            raise Exception
                
        if check_reached_point(goal.x - node.x, goal.y - node.y,MAX_DIFF):
            node.current_point += node.point_counter
            node.point_counter = 1

        speed = adjust_speed(node,angle_to_goal,MAX_DIFF)
        node.publisher.publish(speed)
    except IndexError as err:
        handle_index_error(node,err)
    except Exception as error:
        handle_exception(node,error)