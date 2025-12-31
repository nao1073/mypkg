# mypkg
ロボットシステム学課題2

![test](https://github.com/nao1073/mypkg/actions/workflows/test.yml/badge.svg)

## 事前準備
事前にros2を使える環境にし、以下のコマンドを実行してローカル環境でコマンドを実行できるようにしてください。
```
$ git clone https://github.com/nao1073/mypkg.git
$ colcon build
$ source install/setup.bash
```

## worker_evaluatorコマンド
- workerノード
  - 確率的にタイミングのずれた心拍を模した信号を出力します。
- evalutorノード
  - workerコマンドから受け取った心拍信号の到達間隔からEXCELLENT / WARNING / CRITICALの3段階でタイミングを評価します。
- worker_evaluator　launch
  - workerノードとevaluatorノードを同時に起動・管理するlaunchファイルです。

## 実行方法と出力例
```
$ ros2 launch mypkg worker_evaluator.launch.py
[evaluator-2] [INFO] [1767159470.120806471] [evaluator]: EXCELLENT
```
## 必要なソフトウェア
- Python
  - テスト済みバージョン：3.10
- ROS2 Humble
## テスト環境
- Ubuntu 22.04.5 LTS
- ROS2 Humble
## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。
- © 2025 Nao Takahashi
