"""
A - 深さ優先探索 https://atcoder.jp/contests/atc001/tasks/dfs_a
グリッド DFS
"""
import sys

sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    H, W = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    grid = [list(sys.stdin.readline().split()[0]) for _ in range(H)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    # grid = [
    #     [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    # ]  # int grid

    # logger.debug("{}".format([]))

    d = {"s": 0, "g": 1, ".": 2, "#": 3}

    def dfs(i, j):
        grid[i][j] = 3
        delta_list = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        for delta in delta_list:
            new_i = i + delta[0]
            new_j = j + delta[1]
            if not 0 <= new_i <= H - 1:
                continue
            if not 0 <= new_j <= W - 1:
                continue
            if 1 == grid[new_i][new_j]:
                print("Yes")
                return True

        for delta in delta_list:
            new_i = i + delta[0]
            new_j = j + delta[1]
            if not 0 <= new_i <= H - 1:
                continue
            if not 0 <= new_j <= W - 1:
                continue
            _next = grid[new_i][new_j]

            if _next == 2:
                reached = dfs(new_i, new_j)
                if reached:
                    return True

        return False

    # スタート探す
    to_break = False
    for i in range(H):
        for j in range(W):
            grid[i][j] = d[grid[i][j]]
            if grid[i][j] == 0:
                _i, _j = i, j

    i, j = _i, _j

    reached = dfs(i, j)
    if not reached:
        print("No")


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

    def test_入力例1(self):
        input = """4 5
s####
....#
#####
#...g"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 4
...s
....
....
.g.."""
        output = """Yes"""

        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
###.#.#.#.
#.....#..."""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
#.#.#.#.#.
#.....#..."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """1 10
s..####..g"""
        output = """No"""
        self.assertIO(input, output)
