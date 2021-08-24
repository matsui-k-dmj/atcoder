"""B - 105 https://atcoder.jp/contests/abc106/tasks/abc106_b
"""
import sys

sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def divisor(n: int):
    """1からsqrt(n)までの約数を全部返す
    小さいほうの約数だけが返るので、大きいほうを出す必要があれば割る
    2乗根に注意する

    Args:
        n (int): [description]

    Yields:
        int: [description]
    """
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    # grid = [
    #     [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    # ]  # int grid

    logger.debug("{}".format([]))

    num = 0
    for i in range(1, N + 1, 2):
        div_list = list(divisor(i))
        if len(list(divisor(i))) == 4:
            num += 1

    print(num)


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """105"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7"""
        output = """0"""
        self.assertIO(input, output)
