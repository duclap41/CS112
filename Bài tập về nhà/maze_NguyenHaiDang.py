import heapq

m, n = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(m)]
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

def branch_and_bound(maze, start, end):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False for j in range(n)] for i in range(m)]
    pq = []
    heapq.heappush(pq, (1, start))
    while pq:
        (step, current) = heapq.heappop(pq)
        if current == end:
            return step
        for i in range(4):
            x = current[0] + dx[i]
            y = current[1] + dy[i]
            if x >= 0 and x < m and y >= 0 and y < n and maze[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                heapq.heappush(pq, (step + 1, (x, y)))
    return -1

print(branch_and_bound(maze, start, end))