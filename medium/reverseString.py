def reverse_string(s):
    s = list(s)  # strings are immutable, so convert to list
    left = 0
    right = len(s) - 1

    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]

        # Move pointers
        left += 1
        right -= 1

    return ''.join(s)


# Example
print(reverse_string("hello"))
