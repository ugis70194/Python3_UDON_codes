N ,W = map(int, input().split())
dp = [0]*(W+1)

for _ in range(0, N):
    weight, value = map(int, input().split())
    for w in range(W, weight-1, -1):
        if dp[w-weight] + value > dp[w]:
            dp[w] = dp[w-weight] + value

print(dp[W])