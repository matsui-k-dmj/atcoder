import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    # N = int(sys.stdin.readline().split()[0])  # int 一つ
    N, x = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    s = 0
    for i in range(len(a_list) - 1):
        if a_list[i] + a_list[i + 1] <= x:
            continue
        else:
            r = (a_list[i] + a_list[i + 1]) - x
            a_list[i + 1] = max(0, a_list[i + 1] - r)
            s += r

    print(s)


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
        input = """3 3
2 2 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 1
1 6 1 2 0 4"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 9
3 1 4 1 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 0
5 5"""
        output = """10"""
        self.assertIO(input, output)
