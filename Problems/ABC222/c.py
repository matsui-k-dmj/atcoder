import sys

# sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, M = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    grid = [list(sys.stdin.readline().split()[0]) for _ in range(2 * N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    # logger.debug("{}".format([]))

    rank = range(2 * N)  # i位の人の番号
    win_counts = [0] * (2 * N)  # i番目の人の勝利数
    for j in range(M):
        for k in range(N):
            r1 = 2 * k
            r2 = 2 * k + 1
            n1, n2 = rank[r1], rank[r2]
            a1, a2 = grid[n1][j], grid[n2][j]
            if a1 == a2:
                continue
            elif (
                (a1 == "G" and a2 == "C")
                or (a1 == "C" and a2 == "P")
                or (a1 == "P" and a2 == "G")
            ):
                win_counts[n1] += 1
            else:
                win_counts[n2] += 1

        rank = [
            i[0]
            for i in sorted(
                enumerate(win_counts), key=lambda x: (x[1], -x[0]), reverse=True
            )
        ]

    for r in rank:
        print(r + 1)


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
        input = """2 3
GCP
PPP
CCC
PPC"""
        output = """3
1
2
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2
GC
PG
CG
PP"""
        output = """1
2
3
4"""
        self.assertIO(input, output)
