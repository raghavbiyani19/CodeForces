t=int(input())
while(t!=0):
    n=int(input())
    if(not n & 1):
        n-=1
    print(int(n//2))
    t-=1
