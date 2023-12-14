from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    wheel_velocities_publisher = Node(
        package='wheel_velocities_publisher',
        executable='wheel_velocities_publisher',
        output='screen',
        name='wheel_velocities_publisher',
        emulate_tty=True,
    )

    kinematic_model = Node(
        package='kinematic_model',
        executable='kinematic_model',
        output='screen',
        name='kinematic_model',
        emulate_tty=True,
        
    )

    # create and return launch description object
    return LaunchDescription(
        [
            wheel_velocities_publisher,
            kinematic_model
        ]
    )
