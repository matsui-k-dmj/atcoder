import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import math


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ

    def get_k(n):
        return math.floor((-1 + math.sqrt(1 + 8 * n)) / 2)

    def get_s(k):
        return (k * (k + 1)) // 2

    string = ""
    toggle = True
    while True:
        k = get_k(N)
        string += "7" * k
        s = get_s(k)
        N = N - s
        if N == 0:
            break
        string += "1" if toggle else "2"
        toggle = not toggle

    print(string)

    # logger.debug("{}".format([]))


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest hoge.py
# pypy3 -m unittest hoge.py
