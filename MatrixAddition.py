r, c = map(int, input().split())

# Input first matrix
a = [list(map(int, input().split())) for _ in range(r)]

# Input second matrix
b = [list(map(int, input().split())) for _ in range(r)]

# Add matrices
for i in range(r):
    print([a[i][j] + b[i][j] for j in range(c)])