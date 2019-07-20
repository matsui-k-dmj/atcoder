import sys
sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

import numpy as np


def resolve():
    N = [int(x) for x in sys.stdin.readline().split()][0]
    a_list = [int(x) for x in sys.stdin.readline().split()]

    logger.debug('{} {}'.format(N, a_list))

    box_list = np.zeros(N, dtype=bool)

    for i_box in reversed(range(N)):
        j_arr = np.arange(i_box + 1, N)
        suma = np.sum(box_list[i_box + 1:][np.mod(j_arr + 1, i_box + 1) == 0])
        r = int(suma) % 2
        if r != a_list[i_box]:
            box_list[i_box] = 1

    s = np.sum(box_list)
    print(int(s))

    if s > 0:
        print(' '.join([str(i_box + 1) for i_box in np.arange(N)[box_list]]))


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
1 0 0"""
        output = """1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)
