"""
short test pathが速くても、他の部分が遅いのでTLEする、結局pypyのほうが速い
"""
import sys

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path, dijkstra

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    n, m, s, t = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    grid = np.array([sys.stdin.readline().split() for _ in range(m)], dtype=int).T
    a_mat = csr_matrix((grid[2], grid[:2] - 1), shape=(n, n))
    b_mat = csr_matrix((grid[3], grid[:2] - 1), shape=(n, n))

    from_s_a = dijkstra(a_mat, directed=False, indices=(s - 1))
    from_t_b = dijkstra(b_mat, directed=False, indices=(t - 1))

    logger.debug("{}".format([from_s_a]))
    logger.debug("{}".format([from_t_b]))

    total = from_s_a + from_t_b
    _min = 10 ** 18
    min_cost = [0] * n
    for i in reversed(range(n)):
        if total[i] < _min:
            _min = total[i]
        min_cost[i] = _min

    init = 10 ** 15
    for i in range(n):
        print(int(init - min_cost[i]))


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
        input = """4 3 2 3
1 4 1 100
1 2 1 10
1 3 20 1"""
        output = """999999999999998
999999999999989
999999999999979
999999999999897"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 12 3 8
2 8 685087149 857180777
6 7 298270585 209942236
2 4 346080035 234079976
2 5 131857300 22507157
4 8 30723332 173476334
2 6 480845267 448565596
1 4 181424400 548830121
4 5 57429995 195056405
7 8 160277628 479932440
1 6 475692952 203530153
3 5 336869679 160714712
2 7 389775999 199123879"""
        output = """999999574976994
999999574976994
999999574976994
999999574976994
999999574976994
999999574976994
999999574976994
999999574976994"""
        self.assertIO(input, output)
