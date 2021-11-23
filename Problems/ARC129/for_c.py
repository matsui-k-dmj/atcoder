import math


def get_ans(N):
    def get_k(n):
        return math.floor((-1 + math.sqrt(1 + 8 * n)) / 2)

    def get_s(k):
        return (k * (k + 1)) // 2

    string = ""
    while True:
        k = get_k(N)
        string += "7" * k
        s = get_s(k)
        N = N - s
        if N == 0:
            break
        string += "1"
    return string


def verify(S):
    count = 0
    for i in range(len(S)):
        for j in range(i, len(S)):
            if int(S[i : j + 1]) % 7 == 0:
                count += 1

    return count


for n in range(1000):
    _n = verify(get_ans(n))
    if n != _n:
        print(n, _n)
