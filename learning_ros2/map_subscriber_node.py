

import rclpy

from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid


class MapSubscriber(Node):


    def __init__(self):
        super().__init__('map_subscriber')
        self.subscriber_ = self.create_subscription(
            OccupancyGrid,              # type of subscription
            'map',                      # topic name
            self.map_callback, 
            1)
        # self.subscription 

    def map_callback(self, msg):
        self.get_logger().info(msg.info)




def main(args=None):
    rclpy.init(args=args)

    map_subscriber = MapSubscriber()

    rclpy.spin(map_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    map_subscriber.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()  