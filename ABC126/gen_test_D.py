N = 10**4
with open("test.txt", "w") as f:
    f.write(str(N)+"\n")
    for i in range(N-2):
        f.write("{} {} 2\n".format(i+1, i+2))

    i = N-2
    f.write("{} {} 2".format(i+1, i+2))        