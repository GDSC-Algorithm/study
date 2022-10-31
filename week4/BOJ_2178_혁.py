from collections import deque

n,m = map(int,input().split())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))

#move types
dx = [0,-1,0,1]
dy = [-1,0,1,0]

#최단거리라서 bfs 이용
def bfs(x,y):

    # 큐생성
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

        # graph 밖으로 좌표가 벗어낫을 시에
      if nx < 0 or ny < 0 or nx >=n or ny >=m:
        continue
      if graph[nx][ny] == 0:
        continue
        # 주변 값에 1씩 더해지는 방법으로
      if graph[nx][ny] == 1:
        queue.append((nx,ny))
        graph[nx][ny] = graph[x][y] + 1

    # 좌표의 오른쪽 맨 아래 값 리턴
  return graph[n-1][m-1]

print(bfs(0,0))
