t=int(input())
while(t):
    n=int(input())
    s=str(input())
    ans=0
    for i in range(n):
        if(s[i]=="("):
            ans+=1
        else:
            if(ans>=1):
                ans-=1
    print(ans)
    t-=1
