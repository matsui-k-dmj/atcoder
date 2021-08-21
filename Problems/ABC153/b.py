import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    H, N = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # a_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    s = sum(a_list)

    if s >= H:
        print('Yes')
    else:
        print('No')


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
        input = """10 3
4 5 6"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 3
4 5 6"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """210 5
31 41 59 26 53"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """211 5
31 41 59 26 53"""
        output = """No"""
        self.assertIO(input, output)
