import random
# N = 2000
N = 200000
print(N, N)
for i in range(N):
    print(' '.join(
        [str(random.randint(1, N // 2)),
         str(random.randint(N // 2 + 1, N))]))
