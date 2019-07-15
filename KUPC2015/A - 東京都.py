import sys
sys.setrecursionlimit(4100000)

import re


def resolve():
    T = [int(x) for x in sys.stdin.readline().split()][0]
    s_list = T = [sys.stdin.readline().split()[0] for _ in range(T)]

    # print(s_list)

    pattern = re.compile('tokyo|kyoto')

    for s in s_list:
        count = 0
        while (True):
            match = pattern.search(s)
            if match is None:
                print(count)
                break
            else:
                count += 1
                s = s[match.span()[1]:]


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

    def test_入力例(self):
        input = """5
higashikyoto
kupconsitetokyotokyoto
goodluckandhavefun
a
kyotoa"""
        output = """1
2
0
0
1"""
        self.assertIO(input, output)
