import heapq

# Define the directions we can move in the matrix
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the cost function for a given path
def cost(path):
    return sum(1 for p in path if matrix[p[0]][p[1]] == 1)

# Define the heuristic function for a given path and destination
def heuristic(path, dest):
    return max(abs(dest[0] - path[-1][0]), abs(dest[1] - path[-1][1]))

# Define the search function
def search(matrix, start, dest):
    # Initialize the priority queue with the starting path
    queue = [(heuristic([start], dest), [start])]
    # Initialize the set of visited nodes
    visited = set()

    while queue:
        # Get the path with the lowest cost
        (f, path) = heapq.heappop(queue)

        # Get the last node in the path
        node = path[-1]

        # Check if we have reached the destination
        if node == dest:
            return cost(path)

        # Check if we have already visited this node
        if node in visited:
            continue

        # Add the node to the set of visited nodes
        visited.add(node)

        # Generate the next set of possible paths
        for dir in directions:
            next_node = (node[0] + dir[0], node[1] + dir[1])
            # Check if the next node is within the bounds of the matrix
            if next_node[0] >= 0 and next_node[0] < len(matrix) and next_node[1] >= 0 and next_node[1] < len(matrix[0]):
                # Check if the next node is a 1 and not already visited
                if matrix[next_node[0]][next_node[1]] == 1 and next_node not in visited:
                    # Add the next path to the priority queue
                    new_path = path + [next_node]
                    heapq.heappush(queue, (cost(new_path) + heuristic(new_path, dest), new_path))

    # If we get here, there is no path to the destination
    return -1


r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
start = tuple(map(int, input().split()))
dest = tuple(map(int, input().split()))

result = search(matrix, start, dest)
print(result)
