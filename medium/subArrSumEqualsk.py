def subarray_sum(nums, k):
    count = 0
    curr_sum = 0
    prefix_sum = {0: 1}   # Important

    for num in nums:
        curr_sum += num

        if (curr_sum - k) in prefix_sum:
            count += prefix_sum[curr_sum - k]

        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

    return count


# Example
arr = [1, 2, 3]
k = 3
print(subarray_sum(arr, k))