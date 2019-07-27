with open('./test_D.txt', 'w') as f:
    f.writelines(str(3*10**4)+'\n')
    for i in range(3*10**4-1):
        f.write('{}\n'.format(i+1))
    f.write(str(3*10**4))