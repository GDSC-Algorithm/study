n = int(input())
s, e = map(int, input().split())
m = int(input())


class node:
    def __init__(self, value):
        self.value = value
        self.near = []


graph = [None]

for i in range(1, n + 1):
    graph.append(node(i))

for _ in range(m):
    l, r = map(int, input().split())
    graph[l].near.append(r)
    graph[r].near.append(l)


def bfs(graph, e, s):
    q = [graph[s]]
    dis = [-1 for i in range(n + 1)]
    answer = []
    dis[s] = 0

    while q:
        v = q[0]
        if v not in answer:
            answer.append(v)

            for i in v.near:
                dis[i] = dis[v.value] + 1
                q.append(graph[i])
        del q[0]

    print(dis[e])


bfs(graph, s, e)