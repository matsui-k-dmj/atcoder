import sys
sys.setrecursionlimit(4100000)

import math

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def resolve():
    # S = [x for x in sys.stdin.readline().split()][0]  # 文字列 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]
    grid = [[int(x) for x in sys.stdin.readline().split()]
            for _ in range(3)]  # int grid
    N = [int(x) for x in sys.stdin.readline().split()][0]  # int 一つ
    v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]

    for b in v_list:
        for i in range(3):
            for j in range(3):
                if grid[i][j] == b:
                    grid[i][j] = True

    # 横
    for i in range(3):
        if grid[i][0] == True and grid[i][1] == True and grid[i][2] == True:
            print('Yes')
            return

            # たて
    for j in range(3):
        if grid[0][j] == True and grid[1][j] == True and grid[2][j] == True:
            print('Yes')
            return

    if grid[0][0] == True and grid[1][1] == True and grid[2][2] == True:
        print('Yes')
        return

    if grid[0][2] == True and grid[1][1] == True and grid[2][0] == True:
        print('Yes')
        return

    print('No')


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
        input = """84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """41 7 46
26 89 2
78 92 8
5
6
45
16
57
17"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34"""
        output = """Yes"""
        self.assertIO(input, output)
