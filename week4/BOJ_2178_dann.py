N, M = map(int, input().split())
matrix = [input() for _ in range(N)]  # 표 형식으로 만들기 위해 행렬양식으로 만듬
visited = [[0] * M for _ in range(N)]  # 위와 같은 사이즈의 행렬로, 포인터(cur_loc)이 해당 좌표를 체크했는지 점검해주기 위해 만듬.

cur_loc = [[0, 0]]  # 현재위치를 알려주는 포인터. 내부에 현재 좌표를 넣고 한번에 빼주기 위해 리스트 형식으로 만듬.
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]  # 포인터의 좌우상하 이동

while True:
  cur_x, cur_y = cur_loc[0]
  cur_loc.pop(0)  # cur_loc에 좌표를 넣어주기 위해 내부를 비워둠.
  if cur_x == N - 1 and cur_y == M - 1:  # 좌표가 최우측 최하단(endpoint)에 도달하면 끝내기.
    print(visited[cur_x][cur_y] + 1)
    break
  for i in range(4):  # 현재 좌표에서 상, 하, 좌, 우 각 좌표의 가용여부를 검사하기 위해 4번 반복.
    nx, ny = cur_x + dx[i], cur_y + dy[i]  # 미래 좌표(nx, ny)에 상, 하, 좌, 우를 대입하여 가용여부 검사.
    if 0 <= nx < N and 0 <= ny < M:  # 미래 좌표가 행렬범위를 넘는지 안넘는지 검사.
      if visited[nx][ny] == 0 and matrix[nx][ny] == "1":  # 검사할 좌표 중 방문기록이 없고, 가용한 경로(1)인지 검사
        visited[nx][ny] = visited[cur_x][cur_y] + 1  # 방문기록이 없다면 현재 방문 좌표의 수에 1을 더하여 이동횟수 증가 시킴
        cur_loc.append([nx, ny])  # 현재 좌표를 이동가능한 좌표로 초기화.
