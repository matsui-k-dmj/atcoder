import sys

sys.setrecursionlimit(4100000)
readline = sys.stdin.readline

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    # S = readline().split()[0]  # 文字列 一つ
    # N = int(readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in readline().split()]  # 複数int
    # h_list = [int(x) for x in readline().split()]  # 複数int
    # grid = [list(readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    # grid = [
    #     [int(x) for x in readline().split()] for _ in range(N)
    # ]  # int grid

    logger.debug("{}".format([]))


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる
