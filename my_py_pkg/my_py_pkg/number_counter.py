import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from std_msgs.msg import Int64 



class NumberCounterNode(Node): 
    def __init__(self):
        super().__init__("number_counter") 
        self.counter_= 0
        self.subscriber_ = self.create_subscription(String, "number", self.callback_function, 10)

        self.publisher_ = self.create_publisher(String, "number_count", 10)
        # self.timer_ = self.create_timer(0.5, self.publish_news)

    def callback_function(self, msg: String):
            # self.get_logger().info(msg.data)
            self.counter_+=int(msg.data)
            self.publish_news()


    def publish_news(self):
            msg = String()
            msg.data = f"{self.counter_}"
            self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()