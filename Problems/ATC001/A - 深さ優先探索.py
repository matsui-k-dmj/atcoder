import sys
from io import StringIO
import unittest

import sys
sys.setrecursionlimit(4100000)


def resolve():
    H, W = [int(x) for x in sys.stdin.readline().split()]
    grid = [list(sys.stdin.readline().split()[0]) for _ in range(H)]

    def dfs(i, j):
        if grid[i][j] == 'g':
            return True
        grid[i][j] = "#"

        for delta in [
            (1, 0), (0, -1), (-1, 0), (0, 1)
        ]:  # for dx in [1, 0, -1, 0]: for dy in [0, -1, 0, 1] みたいにできる
            new_i = i + delta[0]
            new_j = j + delta[1]
            if not 0 <= new_i <= H - 1:
                continue
            if not 0 <= new_j <= W - 1:
                continue
            if grid[new_i][new_j] != '#':
                if dfs(new_i, new_j):
                    return True

        return False

    is_break = False
    for i_row in range(H):
        for j_col in range(W):
            if grid[i_row][j_col] == 's':
                success = dfs(i_row, j_col)
                break
        if is_break:
            break

    print("Yes" if success else "No")


if __name__ == "__main__":
    resolve()


# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest template/template.py で実行できる
# pypy3 -m unittest template/template.py で実行できる
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
        input = """4 5
s####
....#
#####
#...g"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4 4
...s
....
....
.g.."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
###.#.#.#.
#.....#..."""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
#.#.#.#.#.
#.....#..."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """1 10
s..####..g"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()