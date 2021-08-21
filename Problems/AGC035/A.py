import sys
sys.setrecursionlimit(4100000)

import numpy as np


def resolve():
    N = [int(x) for x in sys.stdin.readline().split()][0]
    a_list = [int(x) for x in sys.stdin.readline().split()]

    max_len = len(format(max(a_list), 'b'))
    # print('{} {}'.format(N, a_list))
    bin_array = np.array([[int(b) for b in format(a, 'b').zfill(max_len)]
                          for a in a_list])

    # print(bin_array)

    sum_array = bin_array.sum(axis=0)
    # print(sum_array)
    if np.all(sum_array == 0) or np.all(N == 1.5 * sum_array):
        print("Yes")
    else:
        print("No")


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
        input = """3
1 2 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 4 8"""
        output = """No"""
        self.assertIO(input, output)
