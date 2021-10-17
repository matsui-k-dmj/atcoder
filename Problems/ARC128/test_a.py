N = 200000
print(N)
a_list = []
for _ in range(N // 2):
    a_list.append(99999)
    a_list.append(1)
print(" ".join(str(x) for x in a_list))
