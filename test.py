import random
import string
# N = 2000
N = 500000
print(N)
print(''.join([random.choice(string.ascii_lowercase) for _ in range(N)]))
Q = 20000
print(Q)
for _ in range(Q // 2):
    print("{} {} {}".format(1, random.randint(1, N),
                            random.choice(string.ascii_lowercase)))
for _ in range(Q // 2):
    print("{} {} {}".format(2, random.randint(1, N // 2),
                            random.randint(N // 2, N)))