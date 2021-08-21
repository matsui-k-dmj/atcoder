import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    A, B, M = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    b_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    grid = [[int(x) for x in sys.stdin.readline().split()]
            for _ in range(M)]  # int grid

    logger.debug('{}'.format([]))

    _min = min(a_list) + min(b_list)

    for x, y, c in grid:
        a = a_list[x - 1]
        b = b_list[y - 1]

        t = a + b - c
        if _min > t:
            _min = t

    print(_min)


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
        input = """2 3 1
3 3
3 3 3
1 2 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1 2
10
10
1 1 5
1 1 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 1
3 5
3 5
2 2 2"""
        output = """6"""
        self.assertIO(input, output)
