import sys
# sys.setrecursionlimit(4200000)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# import math

from collections import defaultdict

def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    N = int(sys.stdin.readline().split()[0])  # int 一つ
    # N, D = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # a_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int

    d = defaultdict(int)

    for _ in range(N):
        S = sys.stdin.readline().split()[0]  # 文字列 一つ
        d[S] += 1

    _max = 0
    ret = ""
    for k, v in d.items():
        if _max < v:
            _max = v
            ret = k

    print(ret)




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
        input = """5
snuke
snuke
takahashi
takahashi
takahashi"""
        output = """takahashi"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
takahashi
takahashi
aoki
takahashi
snuke"""
        output = """takahashi"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
a"""
        output = """a"""
        self.assertIO(input, output)

