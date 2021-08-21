from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

def main(N, M, a_list):
    div = 10**9 + 7
    a_set = set(a_list)
    @lru_cache(maxsize=None)
    def fib(n):
        if n in a_set:
            return 0
        else:
            if n == -1:
                return 0
            elif n == 0 or n == 1:
                return 1
            else:
                return fib(n-2) % div + fib(n-1)
    
    
    print(fib(N) % div )


if __name__ == "__main__":
    N, M = [int(x) for x in input().split()]
    a_list = []
    for _ in range(M):
        a_list.append(int(input()))

    main(N, M, a_list)
