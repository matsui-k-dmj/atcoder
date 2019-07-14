import sys
sys.setrecursionlimit(4100000)

from collections import deque
from pprint import pprint


def resolve():
    N_ROW, N_COL = [int(x) for x in sys.stdin.readline().split()]
    START_Y, START_X = [int(x)
                        for x in sys.stdin.readline().split()]  # 1 <= <= N_ROW
    GOAL_Y, GOAL_X = [int(x)
                      for x in sys.stdin.readline().split()]  # 1 <= <= N_COL
    grid = [sys.stdin.readline().split()[0] for _ in range(N_ROW)]
    dist_grid = [[10**8] * N_COL for _ in range(N_ROW)]

    # start

    dist_grid[START_Y - 1][START_X - 1] = 0

    queue = deque()
    queue.append((START_Y - 1, START_X - 1))

    delta_list = ((0, 1), (-1, 0), (0, -1), (1, 0))  # y, x

    is_reached = False
    while (queue):
        # pprint(queue)
        # pprint(dist_grid)

        point = queue.popleft()
        current_dist = dist_grid[point[0]][point[1]]
        for dy, dx in delta_list:
            next_y = point[0] + dy
            if not 0 <= next_y <= N_ROW - 1:
                continue
            next_x = point[1] + dx
            if not 0 <= next_x <= N_COL - 1:
                continue
            if next_y == GOAL_Y - 1 and next_x == GOAL_X - 1:
                print(current_dist + 1)
                is_reached = True
                break
            if (grid[next_y][next_x] != '#'
                    and dist_grid[next_y][next_x] > current_dist + 1):
                dist_grid[next_y][next_x] = current_dist + 1
                queue.append((next_y, next_x))

        if is_reached:
            break


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

    def test_入力例1(self):
        input = """7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 8
2 2
2 4
########
#.#....#
#.###..#
#......#
########"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """50 50
2 2
49 49
##################################################
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
##################################################"""
        output = """94"""
        self.assertIO(input, output)
