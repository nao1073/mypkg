#!/bin/bash
# SPDX-FileCopyrightText: 2025 Nao Takahashi
# SPDX-License-Identifier: BSD-3-Clause

dir=~

[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws" || exit 1
colcon build
source "$dir/.bashrc"

timeout 30 ros2 launch mypkg worker_evaluator.launch.py skip_probability:=0.8 > /tmp/mypkg.log 2>&1

grep 'EXCELLENT' /tmp/mypkg.log || exit 1
grep 'WARNING' /tmp/mypkg.log || exit 1
grep 'CRITICAL' /tmp/mypkg.log || exit 1

exit 0
