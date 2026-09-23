#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String



class NumberPublisherNode(Node): 
    def __init__(self):
        super().__init__("number_publisher") 
        # declare the name and the default value
        self.declare_parameter("number", "2")
        self.declare_parameter("timer_period", 1.0)
        self.number_ = self.get_parameter("number").value
        self.timer_period_ = self.get_parameter("timer_period").value
        self.publisher_ = self.create_publisher(String, "number", 10)
        self.timer_ = self.create_timer(self.timer_period_, self.publish_news)

    def publish_news(self):
            msg = String()
            msg.data = self.number_
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()