#include "rclcpp/rclcpp.hpp"

int main(int argc, char **argv){
    //first thing always
    rclcpp::init(argc, argv);

    // auto type
    // shared pointer to Node object
    auto node = std::make_shared<rclcpp::Node>();
    // dot interacts with shared pointer, 
    // arrow interacts with reference to shared pointer
    RCLCPP_INFO(node->get_logger(), "Hello World");

    //last thing always
    rclcpp:shutdown();
    return 0;
}

// how to build code