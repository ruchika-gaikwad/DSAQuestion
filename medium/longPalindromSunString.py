def longestPalindrome(s):
    n = len(s)

    if n == 0:
        return ""

    start = 0
    max_len = 1

    def expand(left, right):

        while left >= 0 and right < n and s[left] == s[right]:
            current_len = right - left + 1

            if current_len > max_len_holder[0]:
                max_len_holder[0] = current_len
                max_len_holder[1] = left

            left -= 1
            right += 1

    max_len_holder = [1,0]

    for i in range(n):

        expand(i,i)

        expand(i,i+1)

    start = max_len_holder[1]
    max_len = max_len_holder[0]

    result = ""

    for i in range(start,start+max_len):
        result += s[i]

    return result

# Test
s = "babad"
print(longestPalindrome(s))

s="cbbd"
print(longestPalindrome(s))