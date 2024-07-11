from launch import LaunchDescription
from launch_ros.actions import Node
import random

def generate_launch_description():
    ld = LaunchDescription()

    turtlesim = Node(
        package = "turtlesim",
        executable="turtlesim_node"
    )

    turtle_spawner_node = Node(
        package = "hh_turtle_bot",
        executable = "turtle_spawner",
        parameters = [
            {"spawn_frequency": random.uniform(0.0,3.0)},
            {"turtle_name_prefix": "hh_good_boy"}
        ]
    )

    turtle_control_node = Node(
        package = "hh_turtle_bot",
        executable = "turtlesim_controller",
        parameters=[
            {"catch_closest_turtle_first": True}
        ]
    )

    ld.add_action(turtlesim)
    ld.add_action(turtle_spawner_node)
    ld.add_action(turtle_control_node)
    return ld