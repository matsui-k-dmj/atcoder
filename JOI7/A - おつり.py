import sys
sys.setrecursionlimit(4100000)


def resolve():
    YEN = [int(x) for x in sys.stdin.readline().split()][0]

    otsuri = 1000 - YEN

    coins_list = [500, 100, 50, 10, 5, 1]

    total = 0
    for coin in coins_list:
        c_count = otsuri // coin
        otsuri = otsuri - c_count * coin
        total += c_count
        if otsuri == 0:
            break
    print(total)


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
        input = """380"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """15"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()