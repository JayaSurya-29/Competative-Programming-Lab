from collections import deque
n,m=map(int,input().split())
grid=[[int(x) for x in input().split()]for _ in range(n)]
q=deque()
time,fresh=0,0
for r in range(n):
    for c in range(m):
        if grid[r][c]==1:
            fresh+=1
        if grid[r][c]==2:
            q.append([r,c])
directions=[[0,1],[0,-1],[1,0],[-1,0]]
while q and fresh>0:
    for i in range(len(q)):
        r,c=q.popleft()
        for dr,dc in directions:
            row,col=dr+r,dc+c
            if (row<0 or row==n or col<0 or col==m or grid[row][col]!=1):
                continue
            grid[row][col]=2
            q.append([row,col])
            fresh-=1
    time+=1
print(time if fresh==0 else -1)
