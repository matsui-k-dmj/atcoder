import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math



def resolve():
    S = sys.stdin.readline().split()[0]  # 文字列 一つ
    T = sys.stdin.readline().split()[0]  # 文字列 一つ

    # logger.debug("{}".format([]))

    base = ord('a')
    L = ord('z') - ord('a') + 1
    K = ord(T[0]) - ord(S[0])

    for i in range(len(S)):
        s = S[i]
        n = ord(s) - base
        n += K
        n = n % L
        if n != ord(T[i]) - base:
            print("No")
            return

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
        input = """abc
ijk"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """z
a"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """ppq
qqp"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """atcoder
atcoder"""
        output = """Yes"""
        self.assertIO(input, output)


