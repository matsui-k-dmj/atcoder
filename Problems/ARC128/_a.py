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

    max_gold = 1
    max_silver = 0
    gold_list = []
    silver_list = []
    max_gold_action = []
    max_silver_action = []
    for a in a_list:
        gold = max_silver / a

        silver = a * max_gold

        if gold > max_gold:
            _max_gold_action = max_silver_action + [1]
            max_gold = gold
        else:
            _max_gold_action = max_gold_action + [0]

        if silver > max_silver:
            max_silver_action = max_gold_action + [1]
            max_silver = silver
        else:
            max_silver_action = max_silver_action + [0]

        max_gold_action = _max_gold_action

    print(" ".join(str(p) for p in max_gold_action))


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
