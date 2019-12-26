import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    N, D = [int(x) for x in sys.stdin.readline().split()]

    logger.debug('{} {}'.format(N, D))

    def ceil_int(a, devider):
        """
        floor は a // devider でいい。
        math.floor(a / divedier)　だとオーバーフローしちゃう。
        """

        if (a % devider > 0):
            a_ceil = a // devider + 1
        else:
            a_ceil = a // devider

        return a_ceil

    print(ceil_int(N, 2 * D + 1))


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
        input = """6 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 1"""
        output = """1"""
        self.assertIO(input, output)
