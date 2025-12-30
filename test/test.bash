#!/bin/bash
set -e

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
WS_DIR=$(cd "$SCRIPT_DIR/.." && pwd)
cd "$WS_DIR"

# ROS2 環境を明示的に読み込む
source /opt/ros/humble/setup.bash

# ビルド
colcon build --symlink-install
source install/setup.bash

run_test () {
    local expected=$1
    local skip_prob=$2

    echo "=== Testing skip_probability=$skip_prob, expecting $expected ==="

    timeout 60 ros2 launch mypkg worker_evaluator.launch.py skip_probability:=$skip_prob > /tmp/mypkg.log 2>&1 || true

    echo "--- Log output ---"
    cat /tmp/mypkg.log
    echo "--- End log ---"

    if grep -q "$expected" /tmp/mypkg.log; then
        echo "PASS: Found $expected"
    else
        echo "FAIL: Did not find $expected"
        return 1
    fi
}

# テストケース
run_test EXCELLENT 0.0
run_test WARNING   0.4
run_test CRITICAL  0.8

echo "All tests passed!"

