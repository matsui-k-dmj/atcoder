import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import math

from collections import defaultdict

def resolve():

    H, W = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(H)
    ]  # int grid

    row_dict = defaultdict(int)
    col_dict = defaultdict(int)

    for i_row in range(H):
        for j_col in range(W):
            v = grid[i_row][j_col]
            row_dict[i_row] += v
            col_dict[j_col] += v

    mat = [[0] * W for _ in range(H)]
    for i_row in range(H):
        for j_col in range(W):
            v = grid[i_row][j_col]
            mat[i_row][j_col] = row_dict[i_row] + col_dict[j_col] - v

    for row in mat:
        print(" ".join([str(x) for x in row]))








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
        input = """3 3
1 1 1
1 1 1
1 1 1"""
        output = """5 5 5
5 5 5
5 5 5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
3 1 4 1
5 9 2 6
5 3 5 8
9 7 9 3"""
        output = """28 28 25 26
39 33 40 34
38 38 36 31
41 41 39 43"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 10
31 41 59 26 53 58 97 93 23 84
62 64 33 83 27 95 2 88 41 97"""
        output = """627 629 598 648 592 660 567 653 606 662
623 633 651 618 645 650 689 685 615 676"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 10
83 86 77 65 93 85 86 92 99 71
62 77 90 59 63 76 90 76 72 86
61 68 67 79 82 80 62 73 67 85
79 52 72 58 69 67 93 56 61 92
79 73 71 69 84 87 98 74 65 70
63 76 91 80 56 73 62 70 96 81
55 75 84 77 86 55 96 79 63 57
74 95 82 95 64 67 84 64 93 50
87 58 76 78 88 84 53 51 54 99
82 60 76 68 89 62 76 86 94 89"""
        output = """1479 1471 1546 1500 1518 1488 1551 1466 1502 1546
1414 1394 1447 1420 1462 1411 1461 1396 1443 1445
1388 1376 1443 1373 1416 1380 1462 1372 1421 1419
1345 1367 1413 1369 1404 1368 1406 1364 1402 1387
1416 1417 1485 1429 1460 1419 1472 1417 1469 1480
1410 1392 1443 1396 1466 1411 1486 1399 1416 1447
1397 1372 1429 1378 1415 1408 1431 1369 1428 1450
1419 1393 1472 1401 1478 1437 1484 1425 1439 1498
1366 1390 1438 1378 1414 1380 1475 1398 1438 1409
1425 1442 1492 1442 1467 1456 1506 1417 1452 1473"""
        self.assertIO(input, output)

