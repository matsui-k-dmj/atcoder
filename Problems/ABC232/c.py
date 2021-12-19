import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math

from itertools import permutations



def resolve():

    N, M = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # a_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int
    
    ab_grid = [
        [int(x) - 1 for x in sys.stdin.readline().split()] for _ in range(M)
    ]  # int grid

    cd_grid = [
        [int(x) - 1 for x in sys.stdin.readline().split()] for _ in range(M)
    ]  # int grid

    for permutation in permutations(range(N)):
        not_found = False
        for a, b in ab_grid:
            pa, pb = permutation[a], permutation[b]
            if [pa, pb] not in cd_grid and [pb, pa] not in cd_grid:
                not_found = True
                break
        
        if not not_found:
            print("Yes")
            return

    print("No")
        





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
        input = """4 4
1 2
1 3
1 4
3 4
1 3
1 4
2 3
3 4"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 6
1 2
1 3
1 4
3 4
3 5
4 5
1 2
1 3
1 4
1 5
3 5
4 5"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 0"""
        output = """Yes"""
        self.assertIO(input, output)


