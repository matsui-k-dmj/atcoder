from typing import List

# 再起限界
import sys

sys.setrecursionlimit(4100000)


# 連続する文字のマックスを取る
def count_raw_char(s, char):
    max_len = 0
    current_len = 0
    for c in s:
        if c == char:
            current_len += 1
        else:
            if max_len < current_len:
                max_len = current_len
            current_len = 0

    return max_len


# 配列の初期化
N0, N1, N2, N3 = 5, 6, 8, 9
H, W = 100, 100

vec = [0] * N0

mat = [[0] * W for i in range(H)]

tensor3 = [[[0] * N2 for i in range(N1)] for j in range(N0)]

tensor4 = [[[[0] * N3 for k in range(N2)] for i in range(N1)] for j in range(N0)]


# gcd
from math import gcd

# 累積和, cmd
from itertools import accumulate

a_range = range(1, 11)
b = list(accumulate(a_range))  # type: ignore
print(a_range)
print(b)

# ? の数
"aa?82?".count("?")

# ? の場所

import re

p = re.compile(r"\?")
q_index_list = [m.span()[0] for m in p.finditer("aa?82?")]

# グリッド の for 文
i = 0
j = 0
H, W = 100, 100
grid = [[0] * W for i in range(H)]
delta_list = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for delta in delta_list:
    new_i = i + delta[0]
    new_j = j + delta[1]
    if 0 <= new_i < H and 0 <= new_j < W:
        grid[new_i][new_j]
