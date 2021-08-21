import math
import numpy as np
def main(N, S):
    e_cum_list = []
    w_cum_list = []
    e_sum = 0
    w_sum = 0
    for char in S:
        if char == 'E':
            e_sum +=1
        else:
            w_sum +=1
        e_cum_list.append(e_sum)
        w_cum_list.append(w_sum)

    min_val = 10**6
    for i in range(N):
        
        if i - 1 < 0:
            w_cum = 0
        else:
            w_cum = w_cum_list[i - 1]
        
        e_cum = e_cum_list[-1] - e_cum_list[i]

        ew_sum = e_cum + w_cum
        if ew_sum < min_val:
            min_val = ew_sum

    print(min_val)




if __name__ == "__main__":
    N = int(input())
    S = input()
    
    main(N, S)
