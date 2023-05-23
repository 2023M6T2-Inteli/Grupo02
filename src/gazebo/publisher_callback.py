def calculate_goal(self):
    goal = Point()
    goal.x = self.point_list[self.current_point][0]
    goal.y = self.point_list[self.current_point][1]
    return goal

def calculate_angle_to_goal(self, goal):
    inc_x = goal.x - self.x
    inc_y = goal.y - self.y
    angle_to_goal = atan2(inc_y, inc_x)
    return angle_to_goal

def check_lidar_margin(self):
    return self.lidar_.margem_segura()

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

def handle_index_error(self, err):
    self.current_point = 0
    self.point_counter = 1
    print(err)

def handle_exception(self, error):
    self.point_counter = -1
    self.current_point += self.point_counter

    speed = Twist()
    speed.linear.x = 0.0
    speed.angular.z = 0.3
    self.publisher.publish(speed)
    print(error)

def publisher_callback(self):
    try:
        goal = self.calculate_goal()
        angle_to_goal = self.calculate_angle_to_goal(goal)

        if not self.check_lidar_margin():
            raise Exception
                
        if self.check_reached_point(goal.x - self.x, goal.y - self.y):
            self.current_point += self.point_counter
            self.point_counter = 1

        speed = self.adjust_speed(angle_to_goal)
        self.publisher.publish(speed)
    except IndexError as err:
        self.handle_index_error(err)
    except Exception as error:
        self.handle_exception(error)