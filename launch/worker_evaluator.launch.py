from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    skip_probability = LaunchConfiguration('skip_probability')

    return LaunchDescription([
        DeclareLaunchArgument(
            'skip_probability',
            default_value='0.0',
            description='Probability to skip publishing'
        ),

        Node(
            package='mypkg',
            executable='worker',
            parameters=[
                {'publish_rate': 1.0},
                {'skip_probability': skip_probability},
            ],
        ),

        Node(
            package='mypkg',
            executable='evaluator',
            parameters=[
                {'ok_time': 1.0},
                {'warn_time': 2.0},
            ],
        ),
    ])

