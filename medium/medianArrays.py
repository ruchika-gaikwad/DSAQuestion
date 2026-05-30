def findMedianSortedArrays(nums1, nums2):
    merged = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    n = len(merged)
    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        mid1 = merged[n // 2 - 1]
        mid2 = merged[n // 2]
        return (mid1 + mid2) / 2.0

# Example 1
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))

# Example 2
nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))