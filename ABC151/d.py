"""bfs
"""
import sys
sys.setrecursionlimit(4100000)

import math
from collections import deque

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

I_MIN = 0
I_MAX = 0
J_MIN = 0
J_MAX = 0
I_DELTA = [1, 0, -1, 0]
J_DELTA = [0, -1, 0, 1]
visited_set = set()
grid = None


def resolve():
    global visited_set, I_MAX, J_MAX, grid

    H, W = [int(x) for x in sys.stdin.readline().split()]
    grid = [list(sys.stdin.readline().split()[0]) for _ in range(H)]

    # logger.debug('{}'.format([H, W, grid]))

    I_MAX = H - 1
    J_MAX = W - 1
    queue = deque()

    max_dist = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                queue.append((i, j, 0))
                visited_set.add((i, j))
                while (len(queue) > 0):
                    i, j, dist = queue.popleft()
                    if max_dist < dist:
                        max_dist = dist
                    for d in range(4):
                        i_next = i + I_DELTA[d]
                        j_next = j + J_DELTA[d]
                        if (
                                i_next, j_next
                        ) not in visited_set and I_MIN <= i_next <= I_MAX and J_MIN <= j_next <= J_MAX:
                            visited_set.add((i_next, j_next))
                            s = grid[i_next][j_next]
                            if s == '.':
                                queue.append((i_next, j_next, dist + 1))
                else:
                    visited_set.clear()
    print(max_dist)


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
        input = """3 3
...
...
..."""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
...#.
.#.#.
.#..."""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2
.."""
        output = """1"""
        self.assertIO(input, output)