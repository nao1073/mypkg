#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
WS_DIR=$(cd "$SCRIPT_DIR/.." && pwd)

cd "$WS_DIR" || exit 1

colcon build
source install/setup.bash

run_test () {
  timeout 30 ros2 launch mypkg worker_evaluator.launch.py skip_probability:=$2 > /tmp/mypkg.log 2>&1

  grep -q "$1" /tmp/mypkg.log
}

run_test EXCELLENT 0.0 || exit 1
run_test WARNING   0.4 || exit 1
run_test CRITICAL  0.8 || exit 1

exit 0

