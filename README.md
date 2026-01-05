# mypkg
ロボットシステム学課題2

![test](https://github.com/nao1073/mypkg/actions/workflows/test.yml/badge.svg)

## 概要
ROS2を使用して心拍信号の監視を行うノードです。
  心拍を模した信号を送信するworkerノードと、その到達間隔からEXCELLENT / WARNING / CRITICALの3段階でタイミングを評価するevalutorノードから構成されます。
  二つのノードはworker_evaluator.launchファイルによって同時に起動・管理されています。

トピック
- /heartbeat
  - workerノードから出力される心拍信号
- /evaluation
  - 受け取った心拍信号を評価しevalutorノードから出力される評価結果

実行方法と出力例
```
$ ros2 launch mypkg worker_evaluator.launch.py
[evaluator-2] [WARN] [1767165966.538482116] [evaluator]: WARNING
[evaluator-2] [ERROR] [1767165967.521475955] [evaluator]: CRITICAL
[evaluator-2] [INFO] [1767165968.521262174] [evaluator]: EXCELLENT
[evaluator-2] [INFO] [1767165969.521338456] [evaluator]: EXCELLENT
[evaluator-2] [INFO] [1767165970.523472341] [evaluator]: EXCELLENT
```
## テスト環境
- Python
  - テスト済みバージョン：3.7 ~ 3.10
- Ubuntu 22.04.5 LTS
- ROS2 Humble
## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されています。
- © 2025 Nao Takahashi
