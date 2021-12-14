"""
incorrect...
"""

import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math

from bisect import bisect_right


def resolve():
    N, X = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int


    y_list = []
    i = bisect_right(a_list, X)
    if i == len(a_list):
        i = i - 1
    else:
        y_list.append((a_list[i], 1))
        i = i - 1

    current_x = X
    current_y = 0
    current_n = 0
    while(True):
        a = a_list[i]
        k = current_x // a
        current_n += k
        current_y += a * k
        if current_x % a == 0:
            y_list.append((current_y, current_n))
            break
        
        y_list.append((current_y + a, current_n + 1))

        current_x = current_x - a * k

        i = i - 1

        if i < 0:
            break


    _min = 10 ** 19
    for y, n in y_list:
        current_x = y - X
        current_n = 0
        i = bisect_right(a_list, current_x) - 1
    
        while(True):
            a = a_list[i]
            k = current_x // a
            current_n += k
            if current_x % a == 0:
                n = n + current_n
                if n < _min:
                    _min = n
                break

            current_x = current_x - a * k
            i = i - 1

            if i < 0:
                break

    print(_min)



    
            




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
        input = """3 87
1 10 100"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 49
1 7"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 123456789012345678
1 100 10000 1000000 100000000 10000000000 1000000000000 100000000000000 10000000000000000 1000000000000000000"""
        output = """233"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 87
1 10"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """2 87
1 87"""
        output = """1"""
        self.assertIO(input, output)