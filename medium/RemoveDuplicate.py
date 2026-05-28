def remove_duplicates(arr):
    return list(set(arr))

arr = [1, 2, 2, 3, 4, 4]
print(remove_duplicates(arr))

def find_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
arr = [1, 3, 4, 2, 2]
print(find_duplicate(arr))

# arr = list(map(int, input("Enter array: ").split()))
#
# seen = set()
# duplicates = set()
#
# for num in arr:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)
#
# print("Duplicate elements:", list(duplicates))