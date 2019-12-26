with open('c_test.txt', 'w') as f:
    f.write('5000 5000\n')
    for _ in range(5000):
        f.write('1 1 1 1\n')
    for _ in range(5000 - 1):
        f.write('1 1 1\n')
    f.write('1 1 1')