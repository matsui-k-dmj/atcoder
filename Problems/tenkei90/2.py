"""
002 - Encyclopedia of Parentheses（★3） https://atcoder.jp/contests/typical90/tasks/typical90_b

()は2通りしかないので、bit全探索できる
正しい()の条件は (と)の数が等しい、全てのi で そこまでの( の数のほうが多い

"""

import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

import math

from collections import defaultdict


def resolve():
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    if N % 2 == 1:
        print()
        return

    if N == 2:
        print("()")
        return

    dict_set = defaultdict(set)

    dict_set[2] = set(["()"])

    for i in range(4, N + 1, 2):
        for s in dict_set[i - 2]:
            dict_set[i].add("(" + s + ")")

        for j in range(2, i // 2 + 1, 2):
            for s1 in dict_set[j]:
                for s2 in dict_set[i - j]:
                    dict_set[i].add(s1 + s2)
                    dict_set[i].add(s2 + s1)

    for s in sorted(dict_set[N]):
        print(s)


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
        input = """2"""
        output = """()"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3"""
        output = """"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4"""
        output = """(())
()()"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10"""
        output = """((((()))))
(((()())))
(((())()))
(((()))())
(((())))()
((()(())))
((()()()))
((()())())
((()()))()
((())(()))
((())()())
((())())()
((()))(())
((()))()()
(()((())))
(()(()()))
(()(())())
(()(()))()
(()()(()))
(()()()())
(()()())()
(()())(())
(()())()()
(())((()))
(())(()())
(())(())()
(())()(())
(())()()()
()(((())))
()((()()))
()((())())
()((()))()
()(()(()))
()(()()())
()(()())()
()(())(())
()(())()()
()()((()))
()()(()())
()()(())()
()()()(())
()()()()()"""
        self.assertIO(input, output)
