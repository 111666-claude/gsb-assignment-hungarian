"""最小代价指派（匈牙利算法），只用标准库。

缺陷：solve 用「全局最小元素逐行贪心」占位，遇到冲突只会跳过，结果是次优甚至无解。
"""

import itertools


class AssignmentError(ValueError):
    """输入不合法。缺陷：不带位置。"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


def _check(matrix):
    size = len(matrix)
    if size == 0:
        raise AssignmentError("矩阵不能为空")
    for row in matrix:
        if len(row) != size:
            raise AssignmentError("必须是方阵")
    return size


def brute_force(matrix):
    """暴力枚举所有排列。"""
    size = _check(matrix)
    best, best_order = None, None
    for order in itertools.permutations(range(size)):
        cost = sum(matrix[row][order[row]] for row in range(size))
        if best is None or cost < best:
            best, best_order = cost, order
    return best, list(best_order)


def solve(matrix):
    """缺陷：按「当前剩余的最小元素」逐行贪心指派，不做行/列归约与增广。"""
    size = _check(matrix)
    used_columns = set()
    order = [None] * size
    total = 0
    while True:
        best = None
        for row in range(size):
            if order[row] is not None:
                continue
            for column in range(size):
                if column in used_columns:
                    continue
                if best is None or matrix[row][column] < best[0]:
                    best = (matrix[row][column], row, column)
        if best is None:
            break
        _, row, column = best
        order[row] = column
        used_columns.add(column)
        total += matrix[row][column]
    if any(item is None for item in order):
        raise AssignmentError("贪心没能给出完整指派")
    return total, order
