t=int(input())
while(t!=0):
    n=int(input())
    if((n//2) & 1):
        print("NO")
    else:
        print("YES")
        ans=[]
        count=n//2
        i=2
        while(count!=0):
            ans.append(i)
            i+=2
            count-=1
        count=n//2
        i=1
        while(count!=1):
            ans.append(i)
            i+=2
            count-=1
        ans.append(i+(n//2))
        print(*ans,sep=" ")
        print()
    t-=1
