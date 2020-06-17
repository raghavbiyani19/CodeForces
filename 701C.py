n=int(input())
s=input()
l=[0]*n
for k in set(s): 
    j = -1
    for i in range(n):
        if s[i]==k:
            j = i
        if j==-1:
            l[i]=n
        else:
            l[i]=max(l[i],i-j+1)
print(min(l))
