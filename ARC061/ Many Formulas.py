import sys
from io import StringIO
import unittest

# 再起限界
import sys
sys.setrecursionlimit(4100000)


def resolve():
    original_s = list(sys.stdin.readline().split()[0])
    sum_list = []
    sum_list_append = sum_list.append

    def dfs(s, sum):
        if len(s) == 0:
            sum_list_append(sum)
            return
        if len(s) == 1:
            sum_list_append(sum + int(s[0]))
            return

        dfs(s[1:], sum + int(s[0]))

        dfs([s[0] + s[1]] + s[2:], sum)

    dfs(original_s, 0)
    print(sum(sum_list))


if __name__ == "__main__":
    resolve()


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
        input = """125"""
        output = """176"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9999999999"""
        output = """12656242944"""
        self.assertIO(input, output)
