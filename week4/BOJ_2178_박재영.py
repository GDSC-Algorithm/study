from collections import deque

N, M = map(int, input().split())
matrix = [[0 for _ in range(M)]] * N

for i in range(N):
    num = list(map(int, input()))
    matrix[i] = num

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            elif matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = matrix[x][y] + 1
                print(matrix)
    return matrix[N-1][M-1]

print(bfs(0, 0))

# https://yuna0125.tistory.com/61