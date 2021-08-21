import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
from collections import defaultdict
# d = defaultdict(list)


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

    dist_list = [10**10 for _ in range(N)]

    dist_list[S] = 0

    while (True):
        is_updated = False
        for from_v, to_v, dist in edge_list:  # 有向グラフじゃないのにfrom to は confusingだな
            if dist_list[to_v] > dist_list[from_v] + dist:
                dist_list[to_v] = dist_list[from_v] + dist
                is_updated = True
            elif dist_list[from_v] > dist_list[to_v] + dist:
                dist_list[from_v] = dist_list[to_v] + dist
                is_updated = True

        if not is_updated:
            break

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