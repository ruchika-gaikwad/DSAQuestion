class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


# Driver Code
nums = list(map(int, input("Enter numbers separated by space: ").split()))

obj = Solution()
result = obj.containsDuplicate(nums)

print("Contains Duplicate:", result)