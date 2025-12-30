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
            output='screen',
            emulate_tty=True,   # ← worker にも付けるとより確実
            parameters=[
                {'publish_rate': 1.0},
                {'skip_probability': skip_probability},
            ],
        ),

        Node(
            package='mypkg',
            executable='evaluator',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'ok_time': 1.5},
                {'warn_time': 3.0},
            ],
        ),
    ])

