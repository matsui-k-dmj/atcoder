"""
最長経路はコストを負にしてベルマンフォードで解ける
個の場合は i, j の小さい順に確定できるから普通にfor分で良かった、、、
"""

import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math

def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    H, W = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    grid = [list(sys.stdin.readline().split()[0]) for _ in range(H)]  # 文字列grid

    edge_list = []
    for i_row in range(H):
        for j_col in range(W):
            c = grid[i_row][j_col]
            if c == "#":
                continue
            n = i_row * W + j_col
            
            if j_col + 1 < W:
                right = grid[i_row][j_col + 1]
                if right == ".":
                    edge_list.append((n, i_row * W + j_col + 1, -1))

            if i_row + 1 < H:
                down = grid[i_row+1][j_col]
                if down == ".":
                    edge_list.append((n, (i_row+1)*W + j_col, -1))
    n = H * W
    g = edge_list

    def bellman_ford(s):
        d = [float('inf')]*n # 各頂点への最小コスト
        d[s] = 0 # 自身への距離は0
        for i in range(n):
            update = False # 更新が行われたか
            for x, y, z in g:
                if d[y] > d[x] + z:
                    d[y] = d[x] + z
                    update = True
            if not update:
                break
            # 負閉路が存在
            if i == n - 1:
                return -1
        return d

    dist = bellman_ford(0)
    m = - min(dist)
    print(m + 1)


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
        input = """3 4
.#..
..#.
..##"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
."""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
.....
.....
.....
.....
....."""
        output = """9"""
        self.assertIO(input, output)


