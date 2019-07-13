import math

def main(N):
    print(math.factorial(N) % (10**9+7))

    

if __name__ == "__main__":
    N = int(input())

    main(N)

