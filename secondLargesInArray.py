arr = list(map(int, input().split()))
unique = sorted(set(arr))

if len(unique) < 2:
    print("No second largest element")
else:
    print(unique[-2])