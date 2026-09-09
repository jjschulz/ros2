#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String



class NumberPublisherNode(Node): 
    def __init__(self):
        super().__init__("number_publisher") 
        self.publisher_ = self.create_publisher(String, "number", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)

    def publish_news(self):
            msg = String()
            msg.data = "2"
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()