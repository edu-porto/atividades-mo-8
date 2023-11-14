from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os


def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_gazebo', 'turtlebot3_world.launch.py'],
            output='screen',
        ),

        ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_navigation2', 'navigation2.launch.py', 'use_sim_time:=True', 'map:=../../../../assets/mapa-atv-2.yaml'],
            output='screen',
        ),

        ExecuteProcess(
            cmd=['ros2', 'run', 'navigation', 'script.py'],  # Update to your actual script name
            output='screen',
            prefix='gnome-terminal --'
        ),
        # Run Python script to move TurtleBot3
        Node(
            package='my_navigation',
            executable='my_node',  
            name='my_node',
            output='screen'
        ),
    ])