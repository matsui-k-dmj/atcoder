import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math

from bisect import bisect_left


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, Q = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    x_list = [int(sys.stdin.readline().split()[0]) for _ in range(Q)]  # 縦方向の複数int
    
    a_list = sorted(a_list)

    for x in x_list:
        i = bisect_left(a_list, x)
        print(N - i)



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
        input = """3 1
100 160 130
120"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
1 2 3 4 5
6
5
4
3
2"""
        output = """0
1
2
3
4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
804289384 846930887 681692778 714636916 957747794
424238336
719885387
649760493
596516650
189641422"""
        output = """5
3
5
5
5"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 2
1
1
2"""
        output = """1
0"""
        self.assertIO(input, output)


