import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    ABCD = [x for x in sys.stdin.readline().split()][0]
    A, B, C, D = [int(x) for x in ABCD]
    logger.debug('{}'.format([A, B, C, D]))

    op_list = ["+", "-"]
    for op1 in op_list:
        if op1 == "+":
            s1 = A + B
        else:
            s1 = A - B
        for op2 in op_list:
            if op2 == "+":
                s2 = s1 + C
            else:
                s2 = s1 - C
            for op3 in op_list:
                if op3 == "+":
                    s3 = s2 + D
                else:
                    s3 = s2 - D

                if s3 == 7:
                    print("{}{}{}{}{}{}{}=7".format(A, op1, B, op2, C, op3, D))
                    return


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
        input = """1222"""
        output = """1+2+2+2=7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0290"""
        output = """0-2+9+0=7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3242"""
        output = """3+2+4-2=7"""
        self.assertIO(input, output)
