import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    N, M = [int(x) for x in sys.stdin.readline().split()]
    pS_list = [[x for x in sys.stdin.readline().split()] for _ in range(M)]

    aced_list = [False for _ in range(N)]
    penal_list = [0 for _ in range(N)]
    for p, s in pS_list:
        p = int(p) - 1
        if s == 'AC':
            aced_list[p] = True
        else:
            if not aced_list[p]:
                penal_list[p] += 1

    for i in range(N):
        if not aced_list[i]:
            penal_list[i] = 0

    print(sum(aced_list), sum(penal_list))


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる
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
        input = """2 5
1 WA
1 AC
2 WA
2 AC
2 WA"""
        output = """2 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000 3
7777 AC
7777 AC
7777 AC"""
        output = """1 0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 0"""
        output = """0 0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 5
1 WA
1 AC
2 WA
2 WA
2 WA"""
        output = """1 1"""
        self.assertIO(input, output)