"""
good
- デバッグできた
- エッジケースをテストした。

bad
- 2進数のとり方をググる必要があった。
- 2進数をpaddingする必要があった。
- 最大bitが順番0に当たると勘違い

luck
- 問題が簡単。

next
- 2進数のとり方メモ
"""

import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    n, X = [int(x) for x in sys.stdin.readline().split()]
    a_list = [int(x) for x in sys.stdin.readline().split()]

    logger.debug('{}'.format([n, X, a_list]))

    logger.debug(bin(X))

    binary = bin(X)[2:]

    binary = '0' * (n - len(binary)) + binary

    s = 0
    for i, b in enumerate(binary[::-1]):
        s += int(b) * a_list[i]

    print(s)


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
        input = """4 5
1 10 100 1000"""
        output = """101"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """20 1048575
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"""
        output = """210"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 0
1000 1000 1000 1000"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """1 1
1000"""
        output = """1000"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """3 1
1 10 100"""
        output = """1"""
        self.assertIO(input, output)