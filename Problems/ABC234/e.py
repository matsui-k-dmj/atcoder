    """
    等差数列列挙すれば良かったらしい
    """
import sys
# sys.setrecursionlimit(4200000)

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    X = int(sys.stdin.readline().split()[0])  # int 一つ

    if X <= 9:
        print(X)
        return

    s = str(X)
    d = int(s[1]) - int(s[0])

    while(True):
        while(True):
            new_s = s[0]
            is_ok = True
            for i in range(1, len(s)):
                c = int(s[0]) + d * i
                if 0 <= c <= 9:
                    new_s = new_s + str(c)
                else:
                    is_ok = False
                    break
            
            if is_ok:
                if int(new_s) >= X:
                    print(new_s)
                    return

            d += 1
            if d >= 9:
                break

        if int(s[0]) <= 9:
            s = str(int(s[0])+1) + s[1:]
            d = -9
        else:
            break

    print('1'*(len(s) + 1))


    

        


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
        input = """152"""
        output = """159"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """88"""
        output = """88"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8989898989"""
        output = """9876543210"""
        self.assertIO(input, output)


    def test_入力例_4(self):
        input = """10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """90"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """100"""
        output = """111"""
        self.assertIO(input, output)

    def test_入力例_7(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)