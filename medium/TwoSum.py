def two_sum(nums, target):
    hashmap = {}  # value -> index

    for i in range(len(nums)):
        complement = target - nums[i]

        # Check if complement exists
        if complement in hashmap:
            return [hashmap[complement], i]

        # Store current number
        hashmap[nums[i]] = i

    return []  # if no solution


# Example usage
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))