"""命令行入口：算最小代价指派。"""

import argparse
import sys

from .solve import AssignmentError, brute_force, solve


def parse_matrix(text):
    matrix = []
    for row in text.split(";"):
        row = row.strip()
        if not row:
            continue
        matrix.append([int(field) for field in row.split(",")])
    return matrix


def build_parser():
    parser = argparse.ArgumentParser(prog="assignment-hungarian", description="最小代价指派")
    parser.add_argument("--matrix", help="分号分行、逗号分列，例如 '1,2;2,100'")
    parser.add_argument("--brute", action="store_true", help="同时给暴力最优")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if not args.matrix:
        print("错误：需要 --matrix", file=sys.stderr)
        return 2
    try:
        matrix = parse_matrix(args.matrix)
        total, order = solve(matrix)
    except (AssignmentError, ValueError) as error:
        print("错误：%s" % error, file=sys.stderr)
        return 1
    print("total=%d order=%s" % (total, ",".join(str(item) for item in order)))
    if args.brute:
        best, best_order = brute_force(matrix)
        print("brute=%d order=%s" % (best, ",".join(str(item) for item in best_order)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
