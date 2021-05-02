import sys
import heapq

vertex, edge = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
adj = [[] for i in range(vertex + 1)]
dist = [2147483647] * (vertex + 1)
q = []

for i in range(edge):
    a, b, cost = map(int, sys.stdin.readline().split())
    adj[a].append((b, cost))

dist[start] = 0
heapq.heappush(q, (0, start))
while(len(q) > 0):
    cost, a = heapq.heappop(q)
    if(cost > dist[a]):
        continue

    for x in adj[a]:
        to = x[0]
        dis = x[1] + cost
        if(dis < dist[to]):
            dist[to] = dis
            heapq.heappush(q, (dis, to))

for i in range(1, vertex + 1):
    if(dist[i] == 2147483647):
        print("INF")
    else:
        print(dist[i])
