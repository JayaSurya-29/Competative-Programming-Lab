first_line=input().split()
T=int(first_line[0])
N=int(first_line[1])
grid=[[int(x) for x in input().split()]for _ in range(N)]
dp=[row[:] for row in grid]
for i in range(1,N):
    dp[0][i]+=dp[0][i-1]
    dp[i][0]+=dp[i-1][0]
for i in range(1,N):
    for j in range(1,N):
        dp[i][j]+=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
print(dp[N-1][N-1])
