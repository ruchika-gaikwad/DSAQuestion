def two_Sum(nums, target):
    num_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in num_map:
            return [num_map[complement], i]

        num_map[nums[i]] = i
nums = [3,3]
target = 6
print(two_Sum(nums, target))

#### Solution 2  ######
# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums [i] + nums[j] ==  target:
#                 return[i,j]
#
# # Example 1
# # nums = [2, 7, 11, 15]
# # target = 9
# #
# # #Example 2
# # nums = [3,2,4]
# # target = 6
#
# # Example 2
# nums = [3,3]
# target = 6
# --print(two_sum(nums, target))


