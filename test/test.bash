#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
WS_DIR=$(cd "$SCRIPT_DIR/.." && pwd)


cd "$WS_DIR" || exit 1

colcon build
source install/setup.bash

run_test () {
  EXPECTED=$1
  SKIP_PROB=$2

  timeout 8 ros2 launch $PKG_NAME $LAUNCH_FILE \
    worker_node.skip_probability:=$SKIP_PROB \
    > $LOG_FILE 2>&1

  grep -q "$EXPECTED" $LOG_FILE
}

run_test "EXCELLENT" 0.0 || exit 1
run_test "WARNING"   0.4 || exit 1
run_test "CRITICAL"  0.8 || exit 1

exit 0

