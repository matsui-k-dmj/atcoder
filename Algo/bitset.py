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
def add(s, i):
    return s | (1 << i)

# sからiを除外
def remove(s, i):
    return s & ~(1 << i)

# sにiが入ってるか
def include(s, i):
    return (s >> i) & 1

### 遅いから注意!!! for s in range((1 << N) - 1): の直下で呼ぶべき
def size(s):
    return bin(s).count("1")

# i より小さい要素がすべて入った集合
def get_lower(i):
    return (1 << i) - 1

# eq / lower
get_lower(i+1)



# union
s | s2

# intersection
s & s2



# s の 要素 を列挙する (別に i でループすればいいやろ、、)
def enumerate_factors(s):
    x = s & -s
    while x:
        yield int(math.log2(x))
        x = s & (~s + (x << 1))


# n要素全部が入ってる集合
(1 << n) - 1

# 普通に列挙すると、ある集合が出るまでにその部分集合はすでに出てきてるようになってる！すごい！
# n要素の集合の部分集合の列挙
range(1 << n)

# 全部が入ってる集合を除いた部分集合の列挙
range((1 << n) - 1)
