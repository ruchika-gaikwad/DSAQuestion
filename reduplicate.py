arr = list(map(int, input().split()))
d = set([x for x in arr if arr.count(x) > 1])
print(d)