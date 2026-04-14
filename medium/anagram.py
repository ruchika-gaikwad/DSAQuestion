# def is_anagram(s, t):
#     return sorted(s) == sorted(t)
#
#
# # Example
# print(is_anagram("anagram", "nagaram"))

def is_anagram(s, t):
    return sorted(s) == sorted(t)

# Taking input
s = input("Enter first string: ")
t = input("Enter second string: ")

if is_anagram(s, t):
    print("Anagram")
else:
    print("Not Anagram")