n = int(input())

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# import math
#
# n = int(input("Enter a number: "))
#
# prime = True
#
# if n <= 1:
#     prime = False
#
# for i in range(2, int(math.sqrt(n)) + 1):
#     if n % i == 0:
#         prime = False
#         break
#
# print("Prime" if prime else "Not Prime")