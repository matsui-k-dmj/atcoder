import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    action_list = [0] * N
    min_i = 0
    max_i = 0
    BIG_A = 0
    scoped_max = 1
    scoped_max_i = 0
    max_ratio = 1
    scope_length = 0
    for i, a in enumerate(a_list):
        if a == 1:
            if scope_length >= 2:
                if max_ratio > 1:
                    action_list[min_i] = 1
                    action_list[max_i] = 1
            elif scope_length == 1:
                action_list[i - 1] = 1

            else:
                pass
            min_i = i
            max_i = i
            scoped_max = BIG_A
            scoped_max_i = i
            max_ratio = 1
            scope_length = 0
        else:
            r = scoped_max / a
            if r > max_ratio:
                max_i = i
                min_i = scoped_max_i
                max_ratio = r

            if scoped_max < a:
                scoped_max = a
                scoped_max_i = i

            scope_length += 1

    if scope_length >= 2:
        if max_ratio > 1:
            action_list[min_i] = 1
            action_list[max_i] = 1

    print(" ".join(str(p) for p in action_list))


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
3 5 2"""
        output = """0 1 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1"""
        output = """0 0 0 0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
426877385 186049196 624834740 836880476 19698398 709113743 436942115 436942115 436942115 503843678"""
        output = """1 1 0 1 1 1 1 0 0 0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5
1000000000 1000000000 1000000000 1000000000 1"""
        output = """1 0 0 0 1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """4
99999999 1 99999999 1"""
        output = """1 1 1 1"""
        self.assertIO(input, output)
