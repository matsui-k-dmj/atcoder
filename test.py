import random
N = 10**3
print(N, N)
for i in range(N):
    print(' '.join([str(random.randint(1, 10**9)) for _ in range(N)]))
