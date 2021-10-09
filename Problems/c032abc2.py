"""
C - 列 https://atcoder.jp/contests/abc032/tasks/abc032_c
しゃくとり法

"""
import sys

# sys.setrecursionlimit(4100000)

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, K = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    s_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    if 0 in s_list:
        print(len(s_list))
        return

    # logger.debug("{}".format([]))
    i_end = 0
    prod = 1
    max_length = 0
    end_reached = False
    for i_start in range(N):
        while True:
            i_end += 1
            if i_end == N + 1:
                end_reached = True
                break

            new = s_list[i_end - 1]
            prod *= new
            if prod <= K:
                l = i_end - i_start
                if l > max_length:
                    max_length = l

            else:
                prod /= s_list[i_start]
                break

        if end_reached:
            break
    print(max_length)


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
        input = """7 6
4
3
1
1
2
10
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6 10
10
10
10
10
0
10"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6 9
10
10
10
10
10
10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4 0
1
2
3
4"""
        output = """0"""
        self.assertIO(input, output)
