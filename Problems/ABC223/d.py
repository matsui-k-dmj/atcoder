"""
D - Restricted Permutation https://atcoder.jp/contests/abc223/tasks/abc223_d
トポロジカルソート
答えのリストs
入次数が0のものからsに加えて、辺を削除(対応するノードの入次数を減らす)
入次数が0になってたら、heapに加える

辞書順にするために、ノードの小さいものから使いたいので、heapを使う

O(VlogV + E)

"""

import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import heapq


def resolve():
    N, M = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    out_edge_list = [[] for _ in range(N)]
    indeg_list = [0] * N  # 入次数
    for _ in range(M):
        a, b = [int(x) - 1 for x in sys.stdin.readline().split()]
        out_edge_list[a].append(b)
        indeg_list[b] += 1

    # 入次数が0ならheapに加える
    heap = []
    for i, d in enumerate(indeg_list):
        if d == 0:
            heapq.heappush(heap, i)

    ret_list = []
    while heap:
        u = heapq.heappop(heap)
        ret_list.append(u)
        for child in out_edge_list[u]:
            indeg_list[child] -= 1  # 辺の削除 = 入次数を一つ減らす
            if indeg_list[child] == 0:
                heapq.heappush(heap, child)  # 入次数が0ならheapに加える

    if any(indeg_list):  # 入次数が1以上のノードが残っていると、ループがあるのでトポロジカルソートは不可能
        print("-1")
    else:
        print(" ".join(str(x + 1) for x in ret_list))


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
        input = """4 3
2 1
3 4
2 4"""
        output = """2 1 3 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
1 2
1 2
2 1"""
        output = """-1"""
        self.assertIO(input, output)
