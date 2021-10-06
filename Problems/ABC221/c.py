"""
順列の列挙は
競プロの基本事項確認~順列生成の方法~ - Qiita https://qiita.com/DaikiSuyama/items/2483a1af0af38408317b
>>> import itertools
>>> t=[i for i in range(4)]
>>> itertools.permutations(t)
<itertools.permutations object at 0x104dc0af0>
>>> list(itertools.permutations(t))
[(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 2, 3, 1), (0, 3, 1, 2), (0, 3, 2, 1), (1, 0, 2, 3), (1, 0, 3, 2), (1, 2, 0, 3), (1, 2, 3, 0), (1, 3, 0, 2), (1, 3, 2, 0), (2, 0, 1, 3), (2, 0, 3, 1), (2, 1, 0, 3), (2, 1, 3, 0), (2, 3, 0, 1), (2, 3, 1, 0), (3, 0, 1, 2), (3, 0, 2, 1), (3, 1, 0, 2), (3, 1, 2, 0), (3, 2, 0, 1), (3, 2, 1, 0)]
>>> list(itertools.permutations(t,2))
[(3, 2), (3, 1), (3, 0), (2, 3), (2, 1), (2, 0), (1, 3), (1, 2), (1, 0), (0, 3), (0, 2), (0, 1)]


"""

import sys

# sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

from itertools import combinations


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

    # edge_list = [[] for _ in range(N)]
    # for _ in range(M):
    #     a, b = [int(x) - 1 for x in sys.stdin.readline().split()]
    #     edge_list[a].append(b)
    #     edge_list[b].append(a)

    # logger.debug("{}".format([]))

    n_chars = len(str(N))
    str_N = str(N)
    _max = 0
    for s in range(1, (1 << n_chars) - 1):
        a_list = []
        b_list = []
        for i in range(n_chars):
            if (s >> i) & 1:
                a_list.append(str_N[i])
            else:
                b_list.append(str_N[i])

        a = sorted(a_list, reverse=True)  # 先にソートしといても良かった
        b = sorted(b_list, reverse=True)

        if a[0] == "0" or b[0] == "0":
            continue

        c = int("".join(a)) * int("".join(b))
        if c > _max:
            _max = c

    print(_max)


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
        input = """123"""
        output = """63"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1010"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """998244353"""
        output = """939337176"""
        self.assertIO(input, output)
