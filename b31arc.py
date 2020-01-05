"""grid, dfs
"""

import sys
sys.setrecursionlimit(4100000)

import math

import logging

from copy import deepcopy

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

LAND = 'o'
SEA = 'x'


def resolve():
    X = [[s for s in [x for x in sys.stdin.readline().split()][0]]
         for _ in range(10)]
    # logger.debug('{}'.format([X]))

    for i in range(10):
        for j in range(10):
            _X = dfs(i, j, deepcopy(X))
            # if i == 5 and j == 4:
            #     logger.debug('{}'.format([i, j, _X]))
            if all([all([s == SEA for s in x]) for x in _X]):
                print('YES')
                return

    print('NO')


# def dfs(i, j, _X):
#     if i + 1 < 10 and _X[i + 1][j] == LAND:
#         _X[i + 1][j] = SEA
#         _X = dfs(i + 1, j, _X)
#     if i - 1 >= 0 and _X[i - 1][j] == LAND:
#         _X[i - 1][j] = SEA
#         _X = dfs(i - 1, j, _X)
#     if j + 1 < 10 and _X[i][j + 1] == LAND:
#         _X[i][j + 1] = SEA
#         _X = dfs(i, j + 1, _X)
#     if j - 1 >= 0 and _X[i][j - 1] == LAND:
#         _X[i][j - 1] = SEA
#         _X = dfs(i, j - 1, _X)
#     return _X

I_MIN = 0
I_MAX = 9
J_MIN = 0
J_MAX = 9
I_DELTA = [1, 0, -1, 0]
J_DELTA = [0, -1, 0, 1]


def dfs(i, j, _X):
    for d in range(4):
        i_next = i + I_DELTA[d]
        j_next = j + J_DELTA[d]
        if I_MIN <= i_next <= I_MAX and J_MIN <= j_next <= J_MAX:
            s = _X[i_next][j_next]
            if s == LAND:
                _X[i_next][j_next] = SEA
                _X = dfs(i_next, j_next, _X)

    return _X


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

    def test_入力例1(self):
        input = """xxxxxxxxxx
xoooooooxx
xxoooooxxx
xxxoooxxxx
xxxxoxxxxx
xxxxxxxxxx
xxxxoxxxxx
xxxoooxxxx
xxoooooxxx
xxxxxxxxxx"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """xxxxxxxxxx
xoooooooxx
xxoooooxxx
xxxoooxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxxxxxxxx
xxxoooxxxx
xxoooooxxx
xxxxxxxxxx"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
ooooxooooo
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx
xxxxoxxxxx"""
        output = """YES"""
        self.assertIO(input, output)
