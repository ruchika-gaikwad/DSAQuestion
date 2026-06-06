class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        # Skip spaces at the end
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            return length

s = input("Enter a string: ")
obj = Solution()
result = obj.lengthOfLastWord(s)
print("Length of last word:", result)