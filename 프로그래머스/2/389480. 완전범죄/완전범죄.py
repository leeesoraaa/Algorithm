def solution(info, n, m):
    from math import inf
    length = len(info)
    dp = [[inf]*m for _ in range(length + 1)]
    dp[0][0]=0
    
    for i in range(length):
        a_trace, b_trace = info[i]
        
        for b_used in range(m):
            
            if dp[i][b_used] == inf:
                continue
                
            if dp[i][b_used] + a_trace < n:
                dp[i+1][b_used] = min(dp[i+1][b_used], dp[i][b_used]+a_trace)
                
            if b_used + b_trace < m:
                dp[i+1][b_used+b_trace] = min(dp[i+1][b_used+b_trace], dp[i][b_used])
        
    result = min(dp[length])
    return result if result < n else -1