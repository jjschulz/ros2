#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from example_interfaces.msg import String

#subscriber for the robot news station
class SmartphoneNode(Node):
    def __init__(self):
        super().__init__("smartphone")
        # type, tpoic name (use the same name as the publisher), callback
        self.subscriber_ = self.create_subscription(String, "robot_news", self.callback_robot_news, 10)

    def callback_robot_news(self, msg: String):
        self.get_logger().info(msg.data)
  
def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()