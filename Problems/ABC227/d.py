"""
2分探索
"""

import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, K = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    def verify(M):
        count = 0
        req = M * K
        for a in a_list:
            count += min(a, M)
            if count >= req:
                return True

        return False

    lb = 0
    ub = 10 ** 20

    while ub - lb > 1:
        mid = (ub + lb) // 2
        if verify(mid):
            lb = mid
        else:
            ub = mid

    print(lb)


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest hoge.py
# pypy3 -m unittest hoge.py

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
        input = """3 3
2 3 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2
1 1 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 3
1 1 3 4"""
        output = """2"""
        self.assertIO(input, output)
