# SPDX-FileCopyrightText: 2025 Nao Takahashi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String
import time

class EvaluatorNode(Node):
    def __init__(self):
        super().__init__('evaluator')

        self.ok_time   = self.declare_parameter('ok_time', 1.5).value
        self.warn_time = self.declare_parameter('warn_time', 3.0).value

        self.last_time = time.time()

        self.create_subscription(Int32, 'heartbeat', self.callback, 10)
        self.create_timer(1.0, self.evaluate)
        self.pub = self.create_publisher(String, 'evaluation', 10)

    def callback(self, _):
        self.last_time = time.time()

    def evaluate(self):
        elapsed = time.time() - self.last_time
        msg = String()

        if elapsed < self.ok_time:
            msg.data = 'EXCELLENT'
            self.get_logger().info(msg.data)
        elif elapsed < self.warn_time:
            msg.data = 'WARNING'
            self.get_logger().warn(msg.data)
        else:
            msg.data = 'CRITICAL'
            self.get_logger().error(msg.data)

        self.pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(EvaluatorNode())
    rclpy.shutdown()

