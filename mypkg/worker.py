import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class WorkerNode(Node):
    def __init__(self):
        super().__init__('worker')

        self.declare_parameter('publish_rate', 1.0)
        self.declare_parameter('skip_probability', 0.3)

        rate = self.get_parameter('publish_rate').value
        self.skip_prob = self.get_parameter('skip_probability').value

        self.publisher_ = self.create_publisher(Int32, 'heartbeat', 10)
        self.timer = self.create_timer(1.0 / rate, self.publish_heartbeat)

    def publish_heartbeat(self):
        if random.random() < self.skip_prob:
            return

        msg = Int32()
        msg.data = 1
        self.publisher_.publish(msg)


def main():
    rclpy.init()
    node = WorkerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

