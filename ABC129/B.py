import numpy as np

def main(w_list):
    cum = np.cumsum(w_list)

    print(min([abs(cum[-1] - 2*cum[i]) for i in range(len(w_list))]))

if __name__ == "__main__":
    N = input()
    w_list = [int(x) for x in input().split()]

    main(w_list)
