import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    N = [int(x) for x in sys.stdin.readline().split()][0]
    a_list = [int(x) for x in sys.stdin.readline().split()]
    b_list = [int(x) for x in sys.stdin.readline().split()]

    count = 0
    for i in range(N)[::-1]:
        a = a_list[i+1]
        b = b_list[i]
        if a >= b:
            count += b
            continue
        else:
            count += a
            b -= a

            if a_list[i] >= b:
                a_list[i] -= b
                count += b
            else:
                count += a_list[i]
                a_list[i] = 0


    print(count)
            





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
        input = """2
3 5 2
4 5"""
        output = """9"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
5 6 3 8
5 100 8"""
        output = """22"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2
100 1 1
1 100"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
1 1
1"""
        output = """1"""
        self.assertIO(input, output)
