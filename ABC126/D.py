import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    N = [int(x) for x in sys.stdin.readline().split()][0]
    edge_list = [[] for _ in range(N)]

    for _ in range(N-1):
        u, v, w = [int(x) for x in sys.stdin.readline().split()]
        edge_list[u-1].append((v-1, w))
        edge_list[v-1].append((u-1, w))

    color_list = [0] * N
    visited_set = set()
    def dfs(i_rec, c_rec):
        visited_set.add(i_rec)
        color_list[i_rec] = c_rec
        for i_next, weight in edge_list[i_rec]:
            if i_next in visited_set:
                continue
            if weight % 2 == 0:
                dfs(i_next, c_rec)
            else:
                dfs(i_next, 1 - c_rec)

    dfs(0, 0)

    for c in color_list:
        print(c)


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
        input = """3
1 2 2
2 3 1"""
        output = """0
0
1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
2 5 2
2 3 10
1 3 8
3 4 2"""
        output = """1
0
1
0
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)
