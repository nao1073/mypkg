import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class WorkerNode(Node):
    def __init__(self):
        super().__init__('worker')

        rate = self.declare_parameter('publish_rate', 1.0).value
        self.skip_prob = self.declare_parameter('skip_probability', 0.3).value

        self.publisher = self.create_publisher(Int32, 'heartbeat', 10)
        self.create_timer(1.0 / rate, self.publish)

    def publish(self):
        if random.random() >= self.skip_prob:
            self.publisher.publish(Int32(data=1))

def main():
    rclpy.init()
    rclpy.spin(WorkerNode())
    rclpy.shutdown()

