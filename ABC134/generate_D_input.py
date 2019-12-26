power = 4
N = 2 * 10**power
text = "1 " * N
text = text[:-1]

with open("test_D_input_{}.txt".format(power), 'w') as f:
    f.write(str(N) + '\n')
    f.write(text)