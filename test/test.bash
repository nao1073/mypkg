#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
WS_DIR=$(cd "$SCRIPT_DIR/.." && pwd)

cd "$WS_DIR" || exit 1

# ビルド
colcon build --symlink-install
source install/setup.bash

# 各評価を確認する関数
run_test () {
    local expected=$1
    local skip_prob=$2

    echo "=== Testing skip_probability=$skip_prob, expecting $expected ==="

    # launch ノード、ログを /tmp/mypkg.log に出力
    timeout 60 ros2 launch mypkg worker_evaluator.launch.py skip_probability:=$skip_prob > /tmp/mypkg.log 2>&1

    # 実際のログを表示
    echo "--- Log output ---"
    cat /tmp/mypkg.log
    echo "--- End log ---"

    # 期待する文字列が出ているか確認
    if grep -q "$expected" /tmp/mypkg.log; then
        echo "PASS: Found $expected"
    else
        echo "FAIL: Did not find $expected"
        return 1
    fi
}

# テストケース
run_test EXCELLENT 0.0 || exit 1
run_test WARNING   0.4 || exit 1
run_test CRITICAL  0.8 || exit 1

echo "All tests passed!"
exit 0

