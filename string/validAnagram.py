def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1

        if count[ch] < 0:
            return False

    for value in count.values():
        if value != 0:
            return False
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))  # True

s = "rat"
t = "car"
print(isAnagram(s, t))  # False