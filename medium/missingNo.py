def find_missing_general(arr):
    n = len(arr) + 1  # total numbers including missing

    total = (min(arr) + max(arr)) * n // 2
    return total - sum(arr)


arr = [7, 8, 9, 10, 12]
print(find_missing_general(arr))