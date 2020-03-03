import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def divisor(n: int):
    """1からsqrt(n)までの約数を全部返す
    
    Args:
        n (int): [description]
    
    Yields:
        int: [description]
    """
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    S = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    if S <= 10**9:
        y = 1
        x = S
        print(' '.join([str(i) for i in [0, 0, x, 0, 0, y]]))
        return

    x = 10**9
    y = math.ceil(S / 10**9)

    a = 1
    b = x * y - S

    logger.debug('{}'.format([x * y - a * b]))

    print(' '.join([str(i) for i in [0, 0, x, a, b, y]]))


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
        input = """3"""
        output = """1 0 2 2 0 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100"""
        output = """0 0 10 0 0 10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """311114770564041497"""
        output = """314159265 358979323 846264338 327950288 419716939 937510582"""
        self.assertIO(input, output)
