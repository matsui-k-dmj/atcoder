import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

from collections import defaultdict

def resolve():
    N, D = [int(x) for x in sys.stdin.readline().split()]

    logger.debug('{} {}'.format(N, D))
    def rec(n_rec, d_rec):
        if n_rec == 1:
            pass

        else:
            suma = 0
            suma += rec(n_rec-1, d_rec)

            for i in range(2,7):
                suma += rec(n_rec-1, d_rec/i)
                
            return suma

    suma = rec(N, D)
    
    print(suma / 6**N)


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
    def test_Sample_Input_1(self):
        input = """2 6"""
        output = """0.416666667"""
        self.assertIO(input, output)
    def test_Sample_Input_2(self):
        input = """3 2"""
        output = """0.875000000"""
        self.assertIO(input, output)
