import sys

# sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


def resolve():
    S = sys.stdin.readline().split()[0]  # 文字列 一つ
    T = sys.stdin.readline().split()[0]  # 文字列 一つ

    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    # grid = [
    #     [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    # ]  # int grid

    # edge_list = [[] for _ in range(N)]
    # for _ in range(M):
    #     a, b = [int(x) - 1 for x in sys.stdin.readline().split()]
    #     edge_list[a].append(b)
    #     edge_list[b].append(a)

    # logger.debug("{}".format([]))

    swapped = False
    for i in range(len(S) - 1):
        if S[i] != T[i] and S[i + 1] == T[i] and S[i] == T[i + 1]:
            swapped = True
            break

    if swapped:
        S = S[:i] + S[i + 1] + S[i] + S[i + 2 :]

    if S == T:
        print("Yes")
    else:
        print("No")


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
        input = """abc
acb"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aabb
bbaa"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcde
abcde"""
        output = """Yes"""
        self.assertIO(input, output)
