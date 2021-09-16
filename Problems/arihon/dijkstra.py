"""dijkstra法
"""

import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from heapq import heappush, heappop


def dijkstra(edge_list, N, s):
    """sからの距離を返す

    Args:
        edge_list (list): list of (v, w)
        N (int): number of vertexes
        s (int): index of start

    Returns:
        list: total cost from the start
    """
    dist = [float("inf")] * N
    dist[s] = 0

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
    N, M = [int(x) for x in sys.stdin.readline().split()]
    s, t = [int(x) for x in sys.stdin.readline().split()]
    edge_list = [[] for _ in range(N)]

    s = s - 1
    t = t - 1

    for _ in range(M):
        u, v, w = [int(x) for x in sys.stdin.readline().split()]
        edge_list[u - 1].append((v - 1, w))
        edge_list[v - 1].append((u - 1, w))

    dist = dijkstra(edge_list, N, s)
    print(dist[t])


if __name__ == "__main__":
    resolve()

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
        input = """2 1
1 2
1 2 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 6
1 4
1 2 1
1 3 5
1 4 4
2 3 1
2 4 5
3 4 1"""
        output = """3"""
        self.assertIO(input, output)
