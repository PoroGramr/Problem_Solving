N = int(input())
data = []
dp = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    data.append(tmp)
    dp.append([-1 for _ in range(len(tmp))])

dp[0][0] = data[0][0]

if N >= 2:
    dp[1][0] = data[0][0] + data[1][0]
    dp[1][1] = data[0][0] + data[1][1]


for i in range(2,N):
    for k in range(len(data[i])):
        if k == 0:
            dp[i][k] = data[i][0] + dp[i-1][0]
        elif k == len(data[i]) - 1:
            dp[i][k] = data[i][k] + dp[i-1][k-1]
        else:
            left = data[i][k] + dp[i-1][k - 1]
            right = data[i][k] + dp[i-1][k]
            dp[i][k] = max(left,right)
        
print(max(dp[N-1]))