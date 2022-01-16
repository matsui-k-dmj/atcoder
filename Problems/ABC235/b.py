import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)




def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    height = h_list[0]
    for h in h_list[1:]:
        if h > height:
            height = h
        else:
            break

    print(height)



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
        input = """5
1 5 10 4 2"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
100 1000 100000"""
        output = """100000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
27 1828 1828 9242"""
        output = """1828"""
        self.assertIO(input, output)

