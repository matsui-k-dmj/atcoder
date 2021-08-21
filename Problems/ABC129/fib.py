fib_memo = {}
fib_memo[1] = 1
fib_memo[2] = 2
def fib(n):
    if n not in fib_memo:
        fib_memo[n] = fib(n-1) + fib(n-2)
    return fib_memo[n]

print(fib(10)) # 55