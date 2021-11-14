"""
001 - Yokan Party（★4） https://atcoder.jp/contests/typical90/tasks/typical90_a
x以下では成立して、x以上では成立しない場合、xの最大値を2分探索で求めれる。
"""
import sys

# sys.setrecursionlimit(4100000)


from bisect import bisect_right

import logging

import heapq


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N, L = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    K = int(sys.stdin.readline().split()[0])  # int 一つ

    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    a_list += [L]

    def verify(m):
        count = 0
        el = 0
        old_a = 0
        for a in a_list:
            el += a - old_a
            old_a = a
            if el >= m:
                count += 1
                el = 0

            if count == K + 1:
                return True

        return False

    lb = 0
    ub = L

    while ub - lb > 1:
        mid = (ub + lb) // 2
        if verify(mid):
            lb = mid
        else:
            ub = mid

    print(lb)


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
        input = """3 34
1
8 13 26"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 45
2
7 11 16 20 28 34 38"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 100
1
28 54 81"""
        output = """46"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3 100
2
28 54 81"""
        output = """26"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """20 1000
4
51 69 102 127 233 295 350 388 417 466 469 523 553 587 720 739 801 855 926 954"""
        output = """170"""
        self.assertIO(input, output)
