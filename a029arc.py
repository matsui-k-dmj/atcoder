"""
さすがに簡単すぎ

"""
import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    N = [int(x) for x in sys.stdin.readline().split()][0]
    t_list = [[int(x) for x in sys.stdin.readline().split()][0]
              for i in range(N)]

    logger.debug('{}'.format([N, t_list]))

    t1 = 0
    t2 = 0
    for t in sorted(t_list, reverse=True):
        if t1 <= t2:
            t1 += t
        else:
            t2 += t

    print(t1 if t1 >= t2 else t2)


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

    def test_入力例1(self):
        input = """4
4
6
7
10"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3
1
2
4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1
29"""
        output = """29"""
        self.assertIO(input, output)
