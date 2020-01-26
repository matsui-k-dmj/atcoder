import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    N, K = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # grid = [[int(x) for x in sys.stdin.readline().split()]
    #         for _ in range(N)]  # int grid

    logger.debug('{}'.format([]))

    h_list = sorted(h_list, reverse=True)

    if len(h_list) <= K:
        print(0)
    else:
        print(sum(h_list[K:]))


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
        input = """3 1
4 1 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 9
7 9 3 2 3 8 4 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 0
1000000000 1000000000 1000000000"""
        output = """3000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()