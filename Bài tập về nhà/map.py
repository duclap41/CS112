def m_coloring_branch_and_bound(graph):
    def is_valid(node, color):
        for i in range(len(graph)):
            if graph[node][i] and colors[i] == color:
                return False
        return True

    def upper_bound(node):
        nonlocal colors, m
        # Use the greedy algorithm to color the remaining nodes
        for i in range(node, len(graph)):
            if colors[i] == -1:
                used_colors = set(colors[j] for j in range(len(graph)) if graph[i][j] and colors[j] != -1)
                unused_colors = set(range(m)) - used_colors
                if len(unused_colors) == 0:
                    return float('inf')  # can't color the remaining nodes
                colors[i] = min(unused_colors)
        return max(colors) + 1

    def backtrack(node):
        nonlocal colors, m, min_colors
        if node == len(graph):
            min_colors = min(min_colors, max(colors) + 1)
            return

        for color in range(m):
            if is_valid(node, color):
                colors[node] = color
                ub = upper_bound(node+1)
                if ub < min_colors:  # prune the search space
                    backtrack(node+1)
                colors[node] = -1

    n = len(graph)
    colors = [-1] * n
    min_colors = float('inf')
    m = n  # start with n colors
    while m > 0:
        backtrack(0)
        if min_colors <= m:
            break
        m -= 1

    return min_colors


n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

best_coloring = m_coloring_branch_and_bound(adj_matrix)
print(best_coloring)