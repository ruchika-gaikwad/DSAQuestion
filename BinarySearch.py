arr = list(map(int, input().split()))
k = int(input())

l, h = 0, len(arr) - 1
f = 0

while l <= h:
    m = (l + h) // 2
    if arr[m] == k:
        f = 1
        break
    elif arr[m] < k:
        l = m + 1
    else:
        h = m - 1

print('Found' if f else 'Not')