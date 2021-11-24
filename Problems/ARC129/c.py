"""
三角数 a_k = k * (k + 1) / 2 = 1辺に石をk個置いて三角形を敷き詰めたときの石の数。= 差分１の等差数列の和でもある。

N以下の最大の三角数は
k*(K+1)/2 <= N
k**2 + k -2N <= 0
式の公式から
floor((-1 + sqrt(1 + 8N) )/ 2)

まあO(sqrt(N))でも求めれる。
"""

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

    # 間違ってる。
    # string = ""
    # toggle = True
    # while True:
    #     k = get_k(N)
    #     string += "7" * k
    #     s = get_s(k)
    #     N = N - s
    #     if N == 0:
    #         break
    #     string += "1" if toggle else "2"
    #     toggle = not toggle

    # print(string)

    # logger.debug("{}".format([]))


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest hoge.py
# pypy3 -m unittest hoge.py
