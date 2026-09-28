# assignment-hungarian

最小代价指派（匈牙利 / KM 算法），只用 Python 标准库。

```
python3 -m hungarian.cli --matrix '1,2;2,100' --brute
python3 -m hungarian.cli --matrix '4,1,3;2,0,5;3,2,2' --brute
python3 -m unittest discover -s tests -v
```

## 口径（README 为准）

- **必须是全局最优**：`--matrix '1,2;2,100'` 按口径是 `total=4`（1→2、2→1），
  现在贪心先抢全局最小的 (0,0)=1，只剩 100，给 `total=101`。
- 算法：行归约 → 列归约 → 用最少的线覆盖所有零 → 对未覆盖元素做增减（匈牙利法），
  或者用势函数 + 增广路（KM）；每轮必须真的增广到所有行都指派上。
- 不变量：结果是一个排列（每行每列各用一次）；`total` 等于所选元素之和；
  与暴力全排列的最优值一致（n ≤ 7 随机矩阵逐例比对，差异必须为 0）；同一矩阵重复求解结果相同。
- 输入校验：必须是方阵、非空、元素为整数；不满足报 `AssignmentError`。
- 规模：n = 200 的随机矩阵要在 1 秒内给出最优指派，内存 O(n²)；不许用全排列暴力。
- 输出：`total=` 与 `order=`（第 i 行选了哪一列），`--brute` 时同时给暴力对照。

## 现在的行为

- `solve` 是「每轮挑当前剩余里最小的元素」的贪心：`1,2;2,100` 给 101（最优 4）。
- 贪心还可能凑不出完整指派（剩下的行没有可用列时直接报错）。
- `brute_force` 是参考实现（全排列），只在 n 小的时候用。

## 计划新增的能力

```
--matrix 矩阵    分号分行、逗号分列
--brute          同时打印暴力最优
```

## 输出

```
total=4 order=1,0
brute=4 order=1,0
```

## 目录

```
hungarian/solve.py   匈牙利法与暴力
hungarian/cli.py     命令行入口
tests/               unittest 用例
```
