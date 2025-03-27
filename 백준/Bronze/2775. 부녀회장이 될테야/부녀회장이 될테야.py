def apartment():
    dp=[[0]*15 for _ in range(15)]

    # 0층(i호 = i명)
    for i in range(1, 15):
        dp[0][i] = i
    
    # 나머지층
    for k in range(1, 15):
        for n in range(1, 15):
            dp[k][n] = dp[k][n-1] + dp[k-1][n]
    return dp

dp = apartment()
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n])