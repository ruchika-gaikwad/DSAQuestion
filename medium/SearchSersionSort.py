class Solution:
    def searchInsert(self, nums, target):
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            i += 1
        return i

nums = list(map(int, input("Enter sorted array elements: ").split()))
target = int(input("Enter target: "))
obj = Solution()
result = obj.searchInsert(nums, target)
print("Insert Position:", result)