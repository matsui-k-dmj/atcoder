import sys
sys.setrecursionlimit(4100000)

import logging

# logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

# @profile
def resolve():
    N_company, M_people = [int(x) for x in sys.stdin.readline().split()]
    company_list = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N_company)]
    people_list = [[int(x) for x in sys.stdin.readline().split()] for _ in range(M_people)]

    logger.debug('{} {}'.format(N_company, M_people))

    N0, N1, N2 = 101, 101, 101
    dp = [[[0] * N2 for i in range(N1)] for j in range(N0)] 
    for company in company_list:
        a, b, c, w = company
        dp[a][b][c] = max(w, dp[a][b][c])

    logger.debug(dp[1][2][3])

    N_levels = 101
    for a in range(N_levels):
        for b in range(N_levels):
            for c in range(N_levels):
                candidate = [dp[a][b][c]]
                if a >= 1:
                    candidate.append(dp[a-1][b][c])
                if b >= 1:
                    candidate.append(dp[a][b-1][c])
                if c >= 1:
                    candidate.append(dp[a][b][c-1])
                dp[a][b][c] = max(candidate)


    for person in people_list:
        print(dp[person[0]][person[1]][person[2]])



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
        input = """3 6
1 2 3 3
3 3 3 6
4 4 4 8
3 4 3
4 4 4
100 100 1
2 3 4
0 0 0
100 100 100"""
        output = """6
8
0
3
0
8"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 6
1 2 3 3
3 3 3 6
4 4 4 8
0 0 0 2
100 100 100 5
3 4 3
4 4 4
100 100 1
2 3 4
0 0 0
100 100 100"""
        output = """6
8
2
3
2
8"""
        self.assertIO(input, output)
