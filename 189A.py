n,a,b,c=map(int,input().split())
ans=0
for x in range(4001):
    for y in range(4001):
        zc=n-(x*a)-(y*b)
        if(zc<0):
            break
        z=zc/c
        if(z==int(z)):
            ans=max(ans,x+y+z)
print(int(ans))
