# Define a function to find a path from a vertex to a vertex using AT
def find_path_AT(start, end, cost_matrix):
    # Initialize an empty path and a queue
    path = []
    queue = [start]
    # Add the start vertex to the queue
    # Loop until the queue is empty or the end vertex is found
    while queue:
        # Pop the first vertex from the queue
        current = queue.pop(0)
        # Add the current vertex to the path
        path.append(current)
        # Check if the current vertex is the end vertex
        if current == end:
            # Return the path and the cost
            return path, sum(cost_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
        # Loop through the adjacent vertices of the current vertex
        for neighbor in range(len(cost_matrix[current])):
            # Check if the neighbor is not in the path and has a positive cost
            if neighbor not in path and cost_matrix[current][neighbor] > 0:
                # Add the neighbor to the queue
                queue.append(neighbor)
    # Return None if no path is found
    return None


# Ask the user to input the number of vertices, the start vertex, the end vertex, and the cost matrix
n = int(input("Enter the number of vertices: "))
start = int(input("Enter the start vertex: "))
end = int(input("Enter the end vertex: "))
# Validate that start and end are within range
if start < 0 or start >= n or end < 0 or end >= n:
    print("Invalid start or end vertex")
else:
    cost_matrix = []
    print("Enter the cost matrix of connections between vertices in a graph:")
    for i in range(n):
        row = list(map(int, input().split()))  # Enter each row as space-separated integers
        cost_matrix.append(row)

# Output
path, cost = find_path_AT(start, end, cost_matrix)
print(f"The path from {start} to {end} is {path} and the cost is {cost}")
