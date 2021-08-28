"""BFS
https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_es
"""
import sys

# sys.setrecursionlimit(4100000)

import math
from collections import deque

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# from pysnooper import snoop


# @snoop()
def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    H, W, N = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    grid = [list(sys.stdin.readline().split()[0]) for _ in range(H)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    # grid = [
    #     [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    # ]  # int grid

    logger.debug("{}".format([]))

    INF = 10e21

    to_break = False
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "S":
                to_break = True
                break

        if to_break:
            break

    I_DELTA = [1, 0, -1, 0]
    J_DELTA = [0, -1, 0, 1]

    d_sum = 0
    for i_cheese in range(1, N + 1):
        dist_mat = [[INF] * W for _ in range(H)]
        dist_mat[i][j] = 0
        deq = deque()
        deq.append((i, j))
        while deq:
            i, j = deq.popleft()
            d = dist_mat[i][j]
            if grid[i][j] == str(i_cheese):
                d_sum += d
                break

            for di, dj in zip(I_DELTA, J_DELTA):
                ni = i + di
                nj = j + dj
                if not 0 <= ni < H or not 0 <= nj < W or grid[ni][nj] == "X":
                    continue
                else:
                    if dist_mat[ni][nj] == INF:
                        dist_mat[ni][nj] = d + 1
                        deq.append((ni, nj))
    print(d_sum)


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
        input = """3 3 1
S..
...
..1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5 2
.X..1
....X
.XX.S
.2.X."""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 9
.X...X.S.X
6..5X..X1X
...XXXX..X
X..9X...X.
8.X2X..X3X
...XX.X4..
XX....7X..
X..X..XX..
X...X.XX..
..X......."""
        output = """91"""
        self.assertIO(input, output)
