from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for i in members[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                queue.append(i)
                # print("i: ", i, "j: ", j)
                # print("node: ", node, "visited[i]: ", visited[i], members)

total = int(input())
a, b = map(int, input().split())
line = int(input())
members = [[] for _ in range(total+1)] # list index out of range 방지
visited = [0] * (total+1)
c = [0] * (total+1)

for _ in range(line):
    i, j = map(int, input().split())
    members[i].append(j)
    members[j].append(i)

bfs(a)
if visited[b] != 0:
    print(visited[b])
else:
    print(-1)
