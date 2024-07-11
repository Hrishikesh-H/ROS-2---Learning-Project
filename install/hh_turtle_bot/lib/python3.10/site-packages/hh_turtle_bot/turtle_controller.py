#!/usr/bin/env python3
import rclpy
import math
from rclpy.node import Node
from functools import partial

# Import necessary message types
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from hh_tt_interfaces.msg import Turtle
from hh_tt_interfaces.msg import TurtleArray
from hh_tt_interfaces.srv import CatchTurtle

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        #PARAMETERS
        self.declare_parameter("catch_closest_turtle_first", True)

        # Initialize variables
        self.pose_ = None
        self.turtle_to_catch_ = None
        self.catch_closet_turtle_first_ = self.get_parameter(
            "catch_closest_turtle_first").value

        # Create publisher for sending velocity commands
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)

        # Create subscriber for receiving turtle's pose updates
        self.pose_subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose, 10)

        # Create subscriber for receiving information about alive turtles
        self.spawn_turtle_sub_ = self.create_subscription(TurtleArray, "alive_turtles", self.callback_alive_turtles, 10)

        # Create a timer to regularly call the control loop
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
   
    def callback_turtle_pose(self, msg):
        """Callback function to update the turtle's pose."""
        self.pose_ = msg
    
    def callback_alive_turtles(self, msg):
        """Callback function to update the list of alive turtles."""
        if len(msg.turtles) > 0:
            if self.catch_closet_turtle_first_:
                closest_turtle = None
                closest_turtle_distance = float('inf')  # Initialize with infinity because None type cannot be compared with float type

                # Find the closest turtle
                for turtle in msg.turtles:
                    dist_x = turtle.x - self.pose_.x
                    dist_y = turtle.y - self.pose_.y
                    distance = math.sqrt(math.pow(dist_x, 2) + math.pow(dist_y, 2))
                    if distance < closest_turtle_distance:
                        closest_turtle = turtle
                        closest_turtle_distance = distance
                self.turtle_to_catch_ = closest_turtle
            else:
                # Select the first turtle in the list if not catching the closest first
                self.turtle_to_catch_ = msg.turtles[0]

    def control_loop(self):
        """Main control loop to move the turtle towards the target."""
        if self.pose_ is None or self.turtle_to_catch_ is None:
            return
        
        # Calculate distance and angle to the target turtle
        dist_x = self.turtle_to_catch_.x - self.pose_.x
        dist_y = self.turtle_to_catch_.y - self.pose_.y
        distance = math.sqrt(math.pow(dist_x, 2) + math.pow(dist_y, 2))

        msg = Twist()

        if distance > 0.5:
            # Move towards the target if far enough
            msg.linear.x = 2 * distance

            # Calculate the angle to the target and adjust orientation
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose_.theta
            if diff > math.pi:
                diff -= 2 * math.pi
            elif diff < -math.pi:
                diff += 2 * math.pi

            msg.angular.z = 6 * diff
        else:
            # Stop moving if close enough and attempt to catch the turtle
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.call_catch_turtle_server(self.turtle_to_catch_.name)
            self.turtle_to_catch_ = None

        # Publish the velocity command
        self.cmd_vel_publisher_.publish(msg)

    def call_catch_turtle_server(self, turtle_name):
        """Call the catch turtle service to catch the specified turtle."""
        catch_client = self.create_client(CatchTurtle, "catch_turtle")
        while not catch_client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for catch service...")
            
        request = CatchTurtle.Request()
        request.name = turtle_name

        # Call the service asynchronously
        future = catch_client.call_async(request)
        future.add_done_callback(partial(self.callback_call_catch_turtle, turtle_name=turtle_name))

    def callback_call_catch_turtle(self, future, turtle_name):
        """Callback function after calling the catch turtle service."""
        try:
            response = future.result()
            if not response.success:
                self.get_logger().error("Turtle " + str(turtle_name) + " could not be caught")
        except Exception as e:
            self.get_logger().error(f"Exception while calling catch service: {e}")

def main(args=None):
    """Main function to initialize and spin the ROS node."""
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
