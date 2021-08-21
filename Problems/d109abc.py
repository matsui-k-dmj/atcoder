"""bfs自体はかけてるからよし！
一筆書きね〜
"""

import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# from collections import defaultdict
# d = defaultdict(list)

# from itertools import combinations
# comb = combinations(range(N), 2)

# 累積和
# from itertools import accumulate
# _list = list(accumulate(a_list)

# from functools import lru_cache
# @lru_cache(maxsize=None)
# def setUp(self):
#     dp.cache_clear()
from collections import deque


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    H, W = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    grid = [[int(x) for x in sys.stdin.readline().split()]
            for _ in range(H)]  # int grid

    logger.debug('{}'.format([]))

    I_MIN = 0
    I_MAX = H - 1
    J_MIN = 0
    J_MAX = W - 1

    delta_i = [0, -1, 0, 1]
    delta_j = [1, 0, -1, 0]

    global_track_list = []
    global_visited_set = set()

    for i_outer in range(H):
        for j_outer in range(W):
            if grid[i_outer][j_outer] % 2 == 1 and (
                    i_outer, j_outer) not in global_visited_set:
                queue = deque()
                queue.append((i_outer, j_outer, []))
                bfs_visited_set = set()
                bfs_visited_set.add((i_outer, j_outer))
                to_break = False
                while (queue):
                    i, j, _track_list = queue.popleft()
                    for d in range(4):
                        i_next = i + delta_i[d]
                        j_next = j + delta_j[d]
                        if I_MIN <= i_next <= I_MAX and J_MIN <= j_next <= J_MAX and (
                                i_next, j_next) not in bfs_visited_set and (
                                    i_next, j_next) not in global_visited_set:
                            bfs_visited_set.add((i_next, j_next))
                            track_list = _track_list.copy()
                            track_list.append((i_next, j_next, i, j))
                            if grid[i_next][j_next] % 2 == 1:
                                # reverse
                                global_track_list += track_list[::-1]
                                for a_next, b_next, a, b in list(
                                        reversed(track_list))[::-1]:
                                    global_visited_set.add((a_next, b_next))
                                    global_visited_set.add((a, b))
                                to_break = True
                                break
                            else:
                                queue.append((i_next, j_next, track_list))

                    if to_break:
                        break

    print(len(global_track_list))
    for t in global_track_list:
        print(' '.join([str(i + 1) for i in t]))


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
        input = """2 3
1 2 3
0 1 1"""
        output = """3
2 2 2 3
1 1 1 2
1 3 1 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
1 0
2 1
1 0"""
        output = """3
1 1 1 2
1 2 2 2
3 1 3 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 5
9 9 9 9 9"""
        output = """2
1 1 1 2
1 3 1 4"""
        self.assertIO(input, output)
