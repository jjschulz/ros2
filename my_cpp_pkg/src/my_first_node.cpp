#include "rclcpp/rclcpp.hpp"

class MyNode : public rclcpp::Node{
    public:
        MyNode() : Node("cpp_test"), counter_(0){
            RCLCPP_INFO(this->get_logger(), "hello World");
            // calls logger every 1 second
            timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&MyNode::timerCallback, this));
        }
    private:
        void timerCallback(){
            RCLCPP_INFO(this->get_logger(), "hello %d", counter_);
            counter_++;
        }
        rclcpp::TimerBase::SharedPtr timer_;
        int counter_;
};

int main(int argc, char **argv){
    //first thing always
    rclcpp::init(argc, argv);

    // auto type
    // shared pointer to Node object
    auto node = std::make_shared<MyNode>();
    // dot interacts with shared pointer, 
    // arrow interacts with reference to shared pointer
    // RCLCPP_INFO(node->get_logger(), "Hello World");

    rclcpp::spin(node);

    //last thing always
    rclcpp::shutdown();
    return 0;
}