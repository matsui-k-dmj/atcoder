import sys


def resolve():
    N_BILLS, YEN_TOTAL = [int(x) for x in sys.stdin.readline().split()]

    is_answer_found = False
    for i_ten in range(N_BILLS + 1):
        for i_five in range(N_BILLS + 1 - i_ten):
            i_one = N_BILLS - i_ten - i_five
            if i_ten * 10000 + i_five * 5000 + i_one * 1000 == YEN_TOTAL:
                is_answer_found = True
                print("{} {} {}".format(i_ten, i_five, i_one))
                break
        if is_answer_found:
            break
    if not is_answer_found:
        print("-1 -1 -1")


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
        input = """9 45000"""
        output = """4 0 5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 196000"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000 1234000"""
        output = """14 27 959"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2000 20000000"""
        output = """2000 0 0"""
        self.assertIO(input, output)
