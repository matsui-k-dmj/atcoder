import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    c = [x for x in sys.stdin.readline().split()][0]  # 整数一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()] # 整数 複数

    logger.debug('{}'.format([c]))

    print(str(chr(ord(c) + 1)))


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
        input = """a"""
        output = """b"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """y"""
        output = """z"""
        self.assertIO(input, output)
