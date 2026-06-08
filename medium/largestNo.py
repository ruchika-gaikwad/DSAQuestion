class Solution:
    def largestNumber(self, nums):


        arr = []
        for num in nums:
            arr.append(str(num))

        n = len(arr)


        for i in range(n):
            for j in range(0, n - i - 1):


                if arr[j] + arr[j + 1] < arr[j + 1] + arr[j]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp


        result = ""
        for item in arr:
            result += item


        if result[0] == '0':
            return "0"

        return result


# Driver Code
nums = [3, 30, 34, 5, 9]

obj = Solution()
print(obj.largestNumber(nums))