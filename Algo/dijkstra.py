import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
from collections import defaultdict
# d = defaultdict(list)


class Heap:
    def __init__(self, _list=None):
        self.heap = []
        if _list is not None:
            for x in _list:
                self.add(x)

    def pop(self):
        if len(self.heap) == 0:
            return
        elif len(self.heap) == 1:
            return self.heap.pop(0)
        retval = self.heap[0]

        self.heap[0] = self.heap.pop(-1)

        i_parent = 0
        while (True):
            is_updated = False
            i_left = 2 * i_parent + 1
            i_right = 2 * i_parent + 2

            # 境界条件
            if i_left >= len(self.heap):
                break
            elif i_right >= len(self.heap):
                i_right = i_left

            # 子供の小さいほうと交代
            if self.heap[i_left] < self.heap[i_right]:
                i_replace = i_left
            else:
                i_replace = i_right

            # 交代
            if self.heap[i_replace] < self.heap[i_parent]:
                is_updated = True
                self.heap[i_parent], self.heap[i_replace] = self.heap[
                    i_replace], self.heap[i_parent]
                i_parent = i_replace

            if not is_updated:
                break

        return retval

    def add(self, x):
        self.heap.append(x)

        i_self = len(self.heap) - 1

        while (True):
            is_updated = False
            i_parent = (i_self - 1) // 2

            # 境界
            if i_parent < 0:
                break

            # 親が自分より小さければ交代
            if self.heap[i_parent] > self.heap[i_self]:
                is_updated = True

                self.heap[i_parent], self.heap[i_self] = self.heap[
                    i_self], self.heap[i_parent]

                i_self = i_parent

            if not is_updated:
                break

    def drain(self):
        while (self.heap):
            yield self.pop()


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    N, E = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    S, G = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    edge_list = [[int(x) for x in sys.stdin.readline().split()]
                 for _ in range(E)]  # int grid

    logger.debug('{}'.format([N, E, S, G, edge_list]))

    neighbour_list = [[] for _ in range(N)]
    for v1, v2, dist in edge_list:
        neighbour_list[v1].append((v2, dist))
        neighbour_list[v2].append((v1, dist))

    dist_list = [10**10 for _ in range(N)]

    dist_list[S] = 0
    used_list = [False for _ in range(N)]
    heap = Heap()
    heap.add((0, 0))

    while (heap.heap):
        dist_from, i_from = heap.pop()
        if used_list[i_from]:
            continue
        else:
            used_list[i_from] = True

        for i_to, delta_dist in neighbour_list[i_from]:
            if used_list[i_to]:
                continue
            old_dist_to = dist_list[i_to]
            new_dist_to = dist_from + delta_dist
            if old_dist_to > new_dist_to:
                dist_list[i_to] = new_dist_to
                heap.add((new_dist_to, i_to))

    print(dist_list[G])


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
        input = """3 3
0 2
0 1 1
0 2 4
1 2 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """7 10
0 6
0 1 2
0 2 5
1 2 4
1 3 6
1 4 10
2 3 2
3 5 1
4 5 3
4 6 5
5 6 9"""
        output = """16"""
        self.assertIO(input, output)