

import rclpy
from rclpy.node import Node

from std_msgs.msg import Header

from nav_msgs.msg import OccupancyGrid


class MapExamplePublisher(Node):

    def __init__(self):
        super().__init__('map_publisher')
        self.publisher_ = self.create_publisher(
            OccupancyGrid,
           'map',
            10
            )
        
        self.publisher_timer = self.create_timer(
            1.0, 
            self.timer_callback
            )
        
        self.i = 0    

        print("MapExamplePublisher initialized")
    
    def timer_callback(self):
        # create a new map message
        map_msg = OccupancyGrid()
        map_msg.header.stamp              = self.get_clock().now().to_msg()
        map_msg.header.frame_id           ='map'
        map_msg.info.map_load_time        = self.get_clock().now().to_msg()
        map_msg.info.resolution           = 0.1
        map_msg.info.width                = 10
        map_msg.info.height               = 10
        map_msg.info.origin.position.x    = 0.0
        map_msg.info.origin.position.y    = 0.0
        map_msg.info.origin.position.z    =  0.0
        map_msg.info.origin.orientation.x = 0.0
        map_msg.info.origin.orientation.y = 0.0
        map_msg.info.origin.orientation.z = 0.0

        map_msg.data = [0] * 10 * 10

        # fill the map data with a pattern
        for i in range(0, 10):
            for j in range(0, 10):
                map_msg.data[i * 10 + j] = (i + j) % 2


        self.i += 1 

        # publish the map message   
        self.publisher_.publish(map_msg)

        self.get_logger().info('Published %d times' % self.i)

    def spin(self):
        rclpy.spin(self)

    def shutdown(self):
        self.publisher_.unregister()
        rclpy.shutdown()




def main(args=None):
    rclpy.init(args=args)
    map_publisher = MapExamplePublisher()
    map_publisher.spin()
    map_publisher.shutdown()
    rclpy.shutdown()



if __name__ == '__main__':
    main()
    