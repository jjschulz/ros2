import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.srv import SetBool



class NumberCounterNode(Node): 
    def __init__(self):
        super().__init__("number_counter") 
        self.counter_= 0
        self.subscriber_ = self.create_subscription(String, "number", self.callback_function, 10)

        self.publisher_ = self.create_publisher(String, "number_count", 10)
        # self.timer_ = self.create_timer(0.5, self.publish_news)

        self.server_ = self.create_service(SetBool, "reset_counter", 
                                                   self.callback_func_reset)
        
    def callback_func_reset(self, request: SetBool.Request, response: SetBool.Response):
        reset_if_true = request.data
        if(reset_if_true):
                self.counter_ = 0
                response.success = True
                self.get_logger().info('resetting counter')
        else:
              response.success = False
        
        # self.get_logger().info(str(request.a)+ "+" + str(request.b) + "=" + str(response.sum))
        return response

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