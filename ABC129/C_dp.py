def main(N, M, a_list):
    div = 10**9 + 7

    a_set = set(a_list)
    
    dp = {}
    dp[0] = 1
    if 1 in a_set:
        dp[1] = 0
    else:
        dp[1] = 1

    for i in range(N):
        if i+2 in a_set:
            dp[i+2] = 0
        else:
            dp[i+2] = (dp[i+1] + dp[i])
    
    print(dp[N] % div)


if __name__ == "__main__":
    N, M = [int(x) for x in input().split()]
    a_list = []
    for _ in range(M):
        a_list.append(int(input()))

    main(N, M, a_list)
