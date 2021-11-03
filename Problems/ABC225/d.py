import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, Q = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # a_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    grid = [
        [int(x) - 1 for x in sys.stdin.readline().split()] for _ in range(Q)
    ]  # int grid

    # edge_list = [[] for _ in range(N)]
    # for _ in range(M):
    #     a, b = [int(x) - 1 for x in sys.stdin.readline().split()]
    #     edge_list[a].append(b)
    #     edge_list[b].append(a)

    # logger.debug("{}".format([]))

    child_list = [-1] * N
    parent_list = [-1] * N
    for q, x, *y in grid:
        if q == 0:
            y = y[0]
            child_list[x] = y
            parent_list[y] = x
        elif q == 1:
            y = y[0]
            child_list[x] = -1
            parent_list[y] = -1
        else:
            childs = []
            childs.append(x + 1)
            n = child_list[x]
            while n != -1:
                childs.append(n + 1)
                n = child_list[n]

            parents = []
            n = parent_list[x]
            while n != -1:
                parents.append(n + 1)
                n = parent_list[n]

            ret = list(reversed(parents)) + childs
            ret = [len(ret)] + ret
            print(" ".join([str(x) for x in ret]))


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
        input = """7 14
1 6 3
1 4 1
1 5 2
1 2 7
1 3 5
3 2
3 4
3 6
2 3 5
2 4 1
1 1 5
3 2
3 4
3 6"""
        output = """5 6 3 5 2 7
2 4 1
5 6 3 5 2 7
4 1 5 2 7
1 4
2 6 3"""
        self.assertIO(input, output)
