"""
でかい数字の演算は時間かかる。頻繁に%とる。

でかい数字の%とるのも時間かかる (10**(10**5) % 13とか)

modの分配法則を使って, 
s = 0
for i in range(10**5):
    s = (s + 10**i) % 13

は
s = 0:
for i in range(10**5):
    s = (s*10 + 1) % 13

とできる。

"""
import sys
sys.setrecursionlimit(4100000)

import logging

# logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

import re

# @profile
def resolve():
    S = sys.stdin.readline().split()[0]

    logger.debug(S)

    dp = [[0] * 13 for i in range(len(S))]
    i = 0
    if S[i] == '?':
        for j in range(10):
            dp[i][j] += 1
    else:
        dp[i][int(S[i])] = 1

    len_S = len(S)
    for i in range(1, len(S)):
        if S[i] == '?':
            for r in range(13):
                dp[i-1][r] %= (10**9 + 7)
                for j in range(10):
                    new_r =  j + r * 10
                    dp[i][new_r % 13] += dp[i-1][r]

        else:
            int_s = int(S[i])
            for r in range(13):
                new_r = int_s + r * 10
                dp[i][new_r % 13] += dp[i-1][r] % (10**9 + 7)

    print(dp[len(S)-1][5] % (10**9 + 7))

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
        input = """??2??5"""
        output = """768"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """?44"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """7?4"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """?6?42???8??2??06243????9??3???7258??5??7???????774????4?1??17???9?5?70???76???"""
        output = """153716888"""
        self.assertIO(input, output)
