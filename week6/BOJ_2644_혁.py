from collections import deque

def bfs(x):

  queue = deque()
  queue.append(x)

  while queue:
    x = queue.popleft()
    for n in graph[x]:
      if fam[n] == 0:
        fam[n] = fam[x] + 1
        queue.append(n)


x = int(input())
graph = [[] for _ in range(x+1)]
p,k = map(int,input().split())
y = int(input())
for _ in range(y):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
  
fam = [0] * (x+1)

bfs(p)

if fam[k] > 0:
  print(fam[k])
else:
  print(-1)
