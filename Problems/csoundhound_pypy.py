"""
D - Saving Snuuk https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d
scipyのshort test pathが速くても、他の部分が遅いのでTLEする、結局pypyのほうが速い
dijkstra

最初のを除いたminとかは、先に後ろからfor文で計算する。
"""
import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from heapq import heappush, heappop


def dijkstra(edge_list, N, s):
    dist = [float("inf")] * N

    class PriorityQueue(object):
        def __init__(self):
            self.queue = []

        def push(self, value):
            heappush(self.queue, value)

        def pop(self):
            return heappop(self.queue)

        def __len__(self):
            return len(self.queue)

        def __contains__(self, item):
            return item in self.queue

    queue = PriorityQueue()

    queue.push((0, s))  # 距離, index
    dist[s] = 0

    while len(queue):
        min_vertex = queue.pop()
        dist_current, i_current = min_vertex
        if dist[i_current] < dist_current:
            continue
        for i_to, cost in edge_list[i_current]:
            new_dist = dist_current + cost
            if new_dist < dist[i_to]:
                dist[i_to] = new_dist
                queue.push((new_dist, i_to))

    return dist


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    n, m, s, t = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    grid = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]
    a_edge_list = [[] for _ in range(n)]
    b_edge_list = [[] for _ in range(n)]
    for u, v, a, b in grid:
        u = u - 1
        v = v - 1

        a_edge_list[u].append((v, a))
        a_edge_list[v].append((u, a))
        b_edge_list[u].append((v, b))
        b_edge_list[v].append((u, b))

    from_s_a = dijkstra(a_edge_list, n, s - 1)
    from_t_b = dijkstra(b_edge_list, n, t - 1)

    _min = 10 ** 18
    min_cost = [0] * n
    for i in reversed(range(n)):
        total = from_s_a[i] + from_t_b[i]
        if total < _min:
            _min = total
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
