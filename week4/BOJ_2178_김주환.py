n,m = map(int,input().split())
check=[[0 for _ in range(m) ] for _ in range(n)]
maze=[]
r=[0,0,-1,1]
c=[-1,1,0,0]
for _ in range(n):
    a = input()
    maze.append(a)

def bfs(y,x):
    q=[[y,x]]
    check[0][0]=1
    while q:
        now=q.pop(0)
        nowy=now[0]
        nowx=now[1]
        for run in range(4):
            nexty=nowy+r[run]
            nextx=nowx+c[run]
            if 0<= nexty <n and 0<= nextx <m:
                if maze[nexty][nextx] == '1' and check[nexty][nextx] == 0:
                    check[nexty][nextx]=check[nowy][nowx] + 1
                    q.append([nexty,nextx])

bfs(0,0)
print(check[n-1][m-1])