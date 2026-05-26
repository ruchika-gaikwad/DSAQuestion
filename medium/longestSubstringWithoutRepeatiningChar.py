def length_of_longest_substring(s):
    seen = {}      # Store character and its latest index
    left = 0       # Start of window
    result = 0     # Maximum length found

    for right in range(len(s)):
        ch = s[right]

        # If character already exists and lies inside current window
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        # Update latest index of character
        seen[ch] = right

        # Calculate current window length
        current_length = right - left + 1

        # Update result without using max()
        if current_length > result:
            result = current_length

    return result


# Example 1
s1 = "abcabcbb"
print("Input:", s1)
print("Output:", length_of_longest_substring(s1))

# Example 2
s2 = "bbbbb"
print("Input:", s2)
print("Output:", length_of_longest_substring(s2))

# Example 3
s3 = "pwwkew"
print("Input:", s3)
print("Output:", length_of_longest_substring(s3))