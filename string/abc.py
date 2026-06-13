n=int(input())
t=n
s=0
while n:
    d=n%10
    s+=d**3
    n//=10
print('Armstrong' if t==s else 'Not')