"""
ビット演算

bitDP
ビットDP
"""
import math
s = 0
n = 10
i = 3
s2 = 2

# 空集合
s = 0

# sにiを追加
s | (1 << i)

# sからiを除外
s & ~(1 << i)

# sにiが入ってるか
(s >> i) & 1

# union
s | s2

# intersection
s & s2

# size
bin(s).count("1")


def enumerate(s):
    x = s & -s
    while x:
        yield int(math.log2(x))
        x = s & (~s + (x << 1))


# n要素全部が入ってる集合
(1 << n) - 1

# n要素の集合の部分集合の列挙
range(1 << n)

# 全部が入ってる集合を除いた部分集合
range((1 << n) - 1)
