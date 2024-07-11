#!/usr/bin/env python3
import rclpy  # ROS 2 Python client library
from rclpy.node import Node  # Base class for ROS 2 nodes
from turtlesim.srv import Spawn  # Service to spawn a turtle in turtlesim
from hh_tt_interfaces.srv import CatchTurtle  # Custom service to catch (remove) a turtle
from turtlesim.srv import Kill  # Service to kill a turtle in turtlesim
from functools import partial  # To create partial functions
import random  # For generating random numbers
import math  # For mathematical functions

from hh_tt_interfaces.msg import Turtle  # Custom message for a single turtle
from hh_tt_interfaces.msg import TurtleArray  # Custom message for an array of turtles

class TurtleSpawnerNode(Node):
    def __init__(self):
        super().__init__("turtle_spawner")  # Initialize the node with the name "turtle_spawner"
        self.declare_parameter("spawn_frequency", 1.0)
        self.declare_parameter("turtle_name_prefix", "hh_turtle")

        self.spawn_frequency_ = self.get_parameter("spawn_frequency").value
        self.turtle_name_prefix_ = self.get_parameter("turtle_name_prefix").value # Prefix for turtle names
        self.turtle_counter_ = 0  # Counter to keep track of the number of spawned turtles
        self.alive_turtles = []  # List to keep track of alive turtles

        # Publisher to publish the array of alive turtles
        self.alive_turtle_publisher_ = self.create_publisher(TurtleArray, "alive_turtles", 10)

        # Timer to periodically spawn a new turtle every 0.5 seconds
        self.spawn_timer_ = self.create_timer(1/self.spawn_frequency_, self.spawn_new_turtle)

        # Service to handle requests to catch (remove) a turtle
        self.catch_turtle_service_ = self.create_service(CatchTurtle, "catch_turtle", self.callback_catch_turtle)
    
    def callback_catch_turtle(self, request, response):
        """Handle catch turtle request by calling the kill server."""
        self.call_kill_server(request.name)
        response.success = True
        return response

    def publish_alive_turtles(self):
        """Publish the list of alive turtles."""
        msg = TurtleArray()
        msg.turtles = self.alive_turtles
        self.alive_turtle_publisher_.publish(msg)

    def spawn_new_turtle(self):
        """Generate a new turtle name and random position, then call the spawn server."""
        self.turtle_counter_ += 1
        name = self.turtle_name_prefix_ + str(self.turtle_counter_)
        x = random.uniform(0.0, 11.0)
        y = random.uniform(0.0, 11.0)
        theta = random.uniform(0.0, 2 * math.pi)
        self.call_spawn_server(name, x, y, theta)

    def call_spawn_server(self, turtle_name, x, y, theta):
        """Create and send a request to the spawn service asynchronously."""
        spawn_client = self.create_client(Spawn, "spawn")
        
        # Wait for the spawn service to become available
        while not spawn_client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for spawn service...")
        
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = turtle_name

        future = spawn_client.call_async(request)
        future.add_done_callback(partial(self.callback_call_spawn, turtle_name=turtle_name, x=x, y=y, theta=theta))

    def callback_call_spawn(self, future, turtle_name, x, y, theta):
        """Process the response from the spawn service."""
        try:
            response = future.result()
            if response.name:
                self.get_logger().info(f"Turtle {response.name} is up baby!!")
                new_turtle = Turtle()
                new_turtle.name = response.name
                new_turtle.x = x
                new_turtle.y = y
                new_turtle.theta = theta
                self.alive_turtles.append(new_turtle)
                self.publish_alive_turtles()
            else:
                self.get_logger().error("Failed to spawn turtle.")
        except Exception as e:
            self.get_logger().error(f"Exception while calling spawn service: {e}")

#-----------------------------------------kill server------------------------------------------------------------#

    def call_kill_server(self, turtle_name):
        """Create and send a request to the kill service asynchronously."""
        kill_client = self.create_client(Kill, "kill")
        
        # Wait for the kill service to become available
        while not kill_client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for kill service...")
        
        request = Kill.Request()
        request.name = turtle_name

        future = kill_client.call_async(request)
        future.add_done_callback(partial(self.callback_call_kill, turtle_name=turtle_name))

    def callback_call_kill(self, future, turtle_name):
        """Process the response from the kill service and update the alive turtles list."""
        try:
            future.result()
            for (i, turtle) in enumerate(self.alive_turtles):
                if turtle.name == turtle_name:
                    del self.alive_turtles[i]
                    self.publish_alive_turtles()
                    break
        except Exception as e:
            self.get_logger().error(f"Exception while calling kill service: {e}")

def main(args=None):
    """Initialize and spin the ROS 2 node."""
    rclpy.init(args=args)
    node = TurtleSpawnerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
