import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import time

class EvaluatorNode(Node):
    def __init__(self):
        super().__init__('evaluator')

        self.declare_parameter('ok_time', 1.5)
        self.declare_parameter('warn_time', 3.0)

        self.ok_time = self.get_parameter('ok_time').value
        self.warn_time = self.get_parameter('warn_time').value

        self.last_time = time.time()

        self.create_subscription(
            Int32,
            'heartbeat',
            self.callback,
            10
        )

        self.timer = self.create_timer(1.0, self.evaluate)

    def callback(self, msg):
        self.last_time = time.time()

    def evaluate(self):
        elapsed = time.time() - self.last_time

        if elapsed < self.ok_time:
            self.get_logger().info('EXCELLENT')
        elif elapsed < self.warn_time:
            self.get_logger().warn('WARNING')
        else:
            self.get_logger().error('CRITICAL')


def main():
    rclpy.init()
    node = EvaluatorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

