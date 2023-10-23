import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='learning_ros2',
            executable='map_publisher_node',
            name='map_publisher_node'
        ),
        launch_ros.actions.Node(
            package='learning_ros2',
            executable='map_subscriber_node',
            name='map_subscriber_node'
        )
    ])
