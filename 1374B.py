t=int(input())
while(t):
    n=int(input())
    ans=0
    while(True):
        if n==1:
            print(ans)
            break
        if n%6==0:
            n=n//6
            ans+=1
        elif(n%3==0):
            n*=2
            ans+=1
        else:
            print(-1)
            break
    t-=1
