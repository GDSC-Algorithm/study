import sys
from collections import deque
input= sys.stdin.readline
arr=[]

n = int(input())
for i in range(n):
    arr.append(list(map(int,input().split())))

shark_body=2

for i in range(n):
    for z in range(n):
        if arr[i][z] == 9:
            shark=[i,z,0]


def bfs(shark) :
    row=[-1,0,1,0]
    col=[0,-1,0,1]
    visited =[[False]*n for _ in range(n)]
    q = deque([shark])
    fish = 1e9
    fish_list=[]

    while q:
        r,c,count = q.popleft()
        for i in range(4):
            if -1<r+row[i] <n \
                    and -1<c+col[i] <n \
                    and arr[r+row[i]][c+col[i]] <= shark_body\
                    and visited[r+row[i]][c+col[i]] == False:
                q.append([r+row[i],c+col[i],count+1])
                visited[r + row[i]][c + col[i]] = True

                if arr[r + row[i]][c + col[i]] < shark_body\
                        and arr[r + row[i]][c + col[i]]!=0:
                    fish = arr[r + row[i]][c + col[i]]
                    fish_list.append([r + row[i],c + col[i],count+1,fish])

    fish_list=sorted(fish_list,key=lambda e: (e[2],e[0],e[1]))
    return fish_list

answer=0
upgrad =0
while True:
    next_shark = bfs(shark)
    if len(next_shark) == 0:
        break
    nr,nc,count,fish = next_shark[0]

    answer+=count
    arr[shark[0]][shark[1]],arr[nr][nc] = 0,0
    shark=[nr,nc,0]

    upgrad+=1
    if upgrad == shark_body:
        upgrad = 0
        shark_body+=1

print(answer)





