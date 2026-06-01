def singleNumber(nums):
    for i in range(len(nums)):
        count = 0

        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1

        if count == 1:
            return nums[i]


nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))




