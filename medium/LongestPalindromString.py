# def rotate_string(s, goal):
#     if len(s) != len(goal):
#         return False
#         return goal in (s + s)
# print(rotate_string("abcde", "cdeab"))

#input from user
s = input().strip()
goal = input().strip()

print("Yes" if len(s)==len(goal) and goal in (s+s) else "No")