def summ(n):
    s=0
    while(n!=0):
        s+= n% 10
        n//= 10
    return s
n=int(input())
x=0
ans=-float('inf')
while(x<=n):
    ans=max(ans,summ(x)+summ(n-x))
    x=x*10+9
print(ans)
