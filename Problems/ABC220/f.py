"""
F - Distance Sums 2 https://atcoder.jp/contests/abc220/tasks/abc220_f

木のある頂点から各頂点への距離はdfsでO(N)
部分木のサイズ(頂点の数)もdfsでO(N)

"""
import sys

sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    # grid = [
    #     [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    # ]  # int grid

    edge_list = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = [int(x) - 1 for x in sys.stdin.readline().split()]
        edge_list[a].append(b)
        edge_list[b].append(a)

    dist0_list = [0] * N
    size_list = [1] * N

    def dfs(i=0, d=0, parent=-1):
        dist0_list[i] = d
        for j in edge_list[i]:
            if j != parent:
                dfs(j, d + 1, i)
                size_list[i] += size_list[j]

    dfs()

    ans_list = [0] * N

    ans_list[0] = sum(dist0_list)

    def dfs2(i, parent):
        ans_list[i] = ans_list[parent] + N - 2 * size_list[i]
        for j in edge_list[i]:
            if j != parent:
                dfs2(j, i)

    for j in edge_list[0]:
        dfs2(j, 0)

    print("\n".join([str(i) for i in ans_list]))

    # logger.debug("{}".format([]))


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
        input = """3
1 2
2 3"""
        output = """3
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 2"""
        output = """1
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 6
1 5
1 3
1 4
1 2"""
        output = """5
9
9
9
9
9"""
        self.assertIO(input, output)
