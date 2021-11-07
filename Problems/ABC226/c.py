from os import get_inheritable
import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from collections import deque


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # a_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    ]  # int grid

    visited_set = set()
    d = deque()
    for s in set(grid[-1][2:]):
        d.append(s)
    while d:
        s = d.pop()
        if s in visited_set:
            continue
        visited_set.add(s)
        for s1 in grid[s - 1][2:]:
            if s1 not in visited_set:
                d.append(s1)

    sum = 0
    for s in visited_set:
        sum += grid[s - 1][0]
    print(sum + grid[-1][0])


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
        input = """3
3 0
5 1 1
7 1 1"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1000000000 0
1000000000 0
1000000000 0
1000000000 0
1000000000 4 1 2 3 4"""
        output = """5000000000"""
        self.assertIO(input, output)
