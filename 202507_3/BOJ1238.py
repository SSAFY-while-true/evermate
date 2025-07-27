# BOJ1238
# 파티

import heapq

def dijkstra(start, graph, n):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq= [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)
        if dist[node] < curr_dist:
            continue
        for cost, next_node in graph[node]:
            new_dist = curr_dist + cost
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

    return dist

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((time, end))

INF = float('inf')

# 왕복 시간
result = [0] * (N + 1)

# 출근
for i in range(1, N + 1):
    if i == X:
        continue
    dist = dijkstra(i, graph, N)
    result[i] += dist[X]

# 퇴근
way_home = dijkstra(X, graph, N)
for i in range(1, N + 1):
    if i == X:
        continue
    result[i] += way_home[i]

print(max(result[1:]))
