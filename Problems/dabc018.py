"""
半分全列挙
D - バレンタインデー https://atcoder.jp/contests/abc018/tasks/abc018_4

部分的に列挙して、残りが貪欲で決まったり、ソートで決まったり、2分探索で決まったりする。
列挙しないと解けなさそうなものは、部分的に列挙してみよう。

"""
import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from itertools import combinations
from collections import defaultdict


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, M, P, Q, R = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(R)
    ]  # int grid
    women_dict = defaultdict(list)
    for x, y, z in grid:
        women_dict[x - 1].append((y - 1, z))

    _max = 0
    for i_list in combinations(range(N), P):
        men_list = [0] * M
        for i_woman in i_list:
            for i_man, z in women_dict[i_woman]:
                men_list[i_man] += z

        s = sum(sorted(men_list, reverse=True)[:Q])
        if s > _max:
            _max = s

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

    def test_入力例1(self):
        input = """3 4 2 3 7
1 1 9
1 2 7
1 3 15
1 4 6
2 2 3
2 4 6
3 3 6"""
        output = """37"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 5 3 2 9
2 3 5
3 1 4
2 2 2
4 1 9
3 5 3
3 3 8
1 4 5
1 5 7
2 4 8"""
        output = """26"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
