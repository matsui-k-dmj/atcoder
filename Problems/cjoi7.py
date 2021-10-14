"""
半分全列挙
重複組み合わせ
"""
import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from itertools import combinations_with_replacement
import bisect


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, M = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    p_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    # logger.debug("{}".format([]))

    p_list = [p for p in p_list if p <= M]

    pairs = combinations_with_replacement([0] + p_list, 2)
    sum_list = [p[0] + p[1] for p in pairs if p[0] + p[1] <= M]
    sum_list = sorted(sum_list)

    _max = 0
    for s in sum_list:
        r = M - s
        i = bisect.bisect_right(sum_list, r) - 1  # r以下の最大のs
        s += sum_list[i]
        if s <= M and _max < s:
            _max = s

    print(_max)


if __name__ == "__main__":
    resolve()
