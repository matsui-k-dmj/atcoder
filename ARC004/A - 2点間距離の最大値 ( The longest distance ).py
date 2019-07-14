import sys
import math


def resolve():
    N = int(sys.stdin.readline().split()[0])
    points_mat = []
    p_append = points_mat.append
    for _ in range(N):
        p_append([float(x) for x in sys.stdin.readline().split()])
    max_dist = 0
    for i in range(N):
        for j in range(N):
            if i >= j:
                continue

            dist = math.sqrt((points_mat[i][0] - points_mat[j][0])**2 +
                             (points_mat[i][1] - points_mat[j][1])**2)

            if dist > max_dist:
                max_dist = dist

    print(max_dist)


if __name__ == "__main__":
    resolve()

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
1 1
2 4
4 3"""
        output = """3.605551"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
1 8
4 0
3 7
2 4
5 9
9 1
6 2
0 2
8 6
7 8"""
        output = """10.630146"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
0 0
0 100
100 0
100 100"""
        output = """141.421356"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5
3 0
1 0
0 0
4 0
2 0"""
        output = """4.000000"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """4
2 2
0 0
1 1
3 3"""
        output = """4.242641"""
        self.assertIO(input, output)