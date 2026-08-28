#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node

#class inherits from Node class, 
#so it will have all the functionality from Node
class MyNode(Node):

    #constructor
    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        #self works the same as 'this'
        #but technically you could name is anything you want
        self.get_logger().info("hello world")
        # just providing a reference to the function, not calling it
        self.create_timer(1.0, self.timer_callback)

    #prints something every 1s
    def timer_callback(self):
        #get_logger is to get the console log kinda, info is to print
        self.get_logger().info("hello" + str(self.counter_))
        self.counter_ +=1



def main(args=None):
    #init first always
    rclpy.init(args=args)

    #create a node
    # node = Node("py_test")
    node = MyNode()

    #info() will print [INFO]
    #node.get_logger().info("Hello world")

    #this keeps the program from ending, so it just hangs there
    #until you ctl+c
    rclpy.spin(node)

    #last line always
    rclpy.shutdown()

if __name__ == "__main__":
    main()