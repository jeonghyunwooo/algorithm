import sys
input = sys.stdin.readline

for test in range(int(input())):
    N = int(input())
    dp = [[0, 0] for _ in range(N + 2)]
    dp[0][0], dp[1][1] = 1, 1
    for i in range(2, N + 1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    print(*dp[N])