import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import math


def resolve():
    S = sys.stdin.readline().split()[0]  # 文字列 一つ

    count = 0
    for i in range(len(S)):
        for j in range(i, len(S)):
            if int(S[i : j + 1]) % 7 == 0:
                count += 1
                print(i, j)
                print(S[i : j + 1])

    print(count)

    # logger.debug("{}".format([]))


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest hoge.py
# pypy3 -m unittest hoge.py
