import math
# Sum of factorials of its digits = the number itself
n = int(input())
t = n
s = 0

while n:
    s += math.factorial(n % 10)
    n //= 10

print('Strong' if t == s else 'Not')
