from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='worker',
            parameters=[
                {'publish_rate': 1.0},
                {'skip_probability': 0.3},
            ],
        ),
        Node(
            package='mypkg',
            executable='evaluator',
            parameters=[
                {'ok_time': 1.5},
                {'warn_time': 3.0},
            ],
        ),
    ])

