#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws" || exit 1
colcon build
source "$dir/.bashrc"

timeout 30 ros2 launch mypkg worker_evaluator.launch.py skip_probability:=0.0 > /tmp/mypkg.log 2>&1

cat /tmp/mypkg.log | grep 'EXCELLENT'

timeout 30 ros2 launch mypkg worker_evaluator.launch.py skip_probability:=0.4 \
  > /tmp/mypkg.log 2>&1
cat /tmp/mypkg.log | grep 'WARNING'

timeout 30 ros2 launch mypkg worker_evaluator.launch.py skip_probability:=0.8 \
  > /tmp/mypkg.log 2>&1
cat /tmp/mypkg.log | grep 'CRITICAL'

