import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from math import ceil


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # a_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(N)
    ]  # int grid

    # edge_list = [[] for _ in range(N)]
    # for _ in range(M):
    #     a, b = [int(x) - 1 for x in sys.stdin.readline().split()]
    #     edge_list[a].append(b)
    #     edge_list[b].append(a)

    # logger.debug("{}".format([]))

    b11 = grid[0][0]

    to_break = False
    old_ceil = ceil(grid[0][0] / 7) - 1
    for i in range(1, len(grid) + 1):
        c = ceil(grid[i - 1][0] / 7)
        if c != old_ceil + 1:
            to_break = True
            break
        old_ceil = c
        for j in range(2, len(grid[0]) + 1):
            if ceil(grid[i - 1][j - 1] / 7) != c:
                to_break = True
                break

        if to_break:
            break

    if to_break:
        print("No")
    else:
        print("Yes")


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
        input = """2 3
1 2 3
8 9 10"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1
1
2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 4
1346 1347 1348 1349
1353 1354 1355 1356
1360 1361 1362 1363
1367 1368 1369 1370
1374 1375 1376 1377
1381 1382 1383 1384
1388 1389 1390 1391
1395 1396 1397 1398
1402 1403 1404 1405
1409 1410 1411 1412"""
        output = """Yes"""
        self.assertIO(input, output)
