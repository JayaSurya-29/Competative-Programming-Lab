first_line=input().split()
V=int(first_line[0])
N=int(first_line[1])
coins=list(map(int,input().split()))
dp=[V+1]*(V+1)
dp[0]=0
for i in range(1,V+1):
    for coin in coins:
        if i>=coin:
            dp[i]=min(dp[i],dp[i-coin]+1)
if dp[V]>V:
    print(-1)
else:
    print(dp[V])
