import random
# N = 2000
N = 3
print(N, N)
for i in range(N):
    print(' '.join([str(random.randint(0, 9)) for _ in range(N)]))
