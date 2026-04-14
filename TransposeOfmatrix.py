r, c = map(int, input().split())
a = [list(map(int, input().split())) for i in range(r)]

for j in range(c):
    print([a[i][j] for i in range(r)])