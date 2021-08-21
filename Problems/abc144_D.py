import sys
sys.setrecursionlimit(4100000)

import logging
import math

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    a, b, x = [float(x) for x in sys.stdin.readline().split()]

    logger.debug([a, b, x])

    y_0 = 2 * x / a**2
    logger.debug(y_0)

    if y_0 >= b:
        if b - x / a**2 == 0:
            print(0)
        else:
            theta = 90 - math.degrees(math.atan(
                (a / 2) * (1 / (b - x / a**2))))
            print(theta)
    else:
        theta = 90 - math.degrees(math.atan(2 * x / (a * (b**2))))
        print(theta)


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py
# pypy3 -m unittest template/template.py
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
        input = """2 2 4"""
        output = """45.0000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12 21 10"""
        output = """89.7834636934"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1 8"""
        output = """4.2363947991"""
        self.assertIO(input, output)
