import sys

# sys.setrecursionlimit(4100000)

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def compress(a_list):
    s = set(a_list)
    return {v: i for i, v in enumerate(sorted(s))}, len(s)


def resolve():
    # S = sys.stdin.readline().split()[0]  # 文字列 一つ
    w, h = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    n = int(sys.stdin.readline().split()[0])  # int 一つ

    # h_list = [int(x) for x in sys.stdin.readline().split()]  # 複数int
    # grid = [list(sys.stdin.readline().split()[0]) for _ in range(N)]  # 文字列grid
    # v_list = [int(sys.stdin.readline().split()[0]) for _ in range(N)]  # 縦方向の複数int

    grid = [
        [int(x) for x in sys.stdin.readline().split()] for _ in range(n)
    ]  # int grid

    x_list = []
    y_list = []
    for x1, y1, x2, y2 in grid:
        if x1 - 1 >= 0:
            x_list.append(x1 - 1)
        x_list.append(x1)
        x_list.append(x2)
        if x2 + 1 <= w:
            x_list.append(x2 + 1)

        if y1 - 1 >= 0:
            y_list.append(y1 - 1)
        y_list.append(y1)
        y_list.append(y2)
        if y2 + 1 <= h:
            y_list.append(y2 + 1)

    x_dict, max_x = compress(x_list)
    y_dict, max_y = compress(y_list)

    H = max_y - 1
    W = max_x - 1

    ita_mat = [[0] * W for _ in range(H)]
    for x1, y1, x2, y2 in grid:
        x1 = x_dict[x1]
        y1 = y_dict[y1]
        x2 = x_dict[x2]
        y2 = y_dict[y2]
        for i_row in range(y1, y2):
            ita_mat[i_row][x1:x2] = [1] * (x2 - x1)

    delta_list = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def dfs(i, j):
        ita_mat[i][j] = 1
        for delta in delta_list:
            new_i = i + delta[0]
            new_j = j + delta[1]
            if not 0 <= new_i <= H - 1:
                continue
            if not 0 <= new_j <= W - 1:
                continue
            if 0 == ita_mat[new_i][new_j]:
                dfs(new_i, new_j)

    count = 0
    for i in range(H):
        for j in range(W):
            if ita_mat[i][j] == 0:
                count += 1
                dfs(i, j)

    print(count)


if __name__ == "__main__":
    resolve()

# AtCoder Unit Test で自動生成できる, 最後のunittest.main は消す
# python -m unittest hoge.py
# pypy3 -m unittest hoge.py
