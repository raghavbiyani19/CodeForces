t=int(input())
while(t!=0):
    s=str(input())
    n=len(s)
    print(s[0],end="")
    for i in range(1,n,2):
        print(s[i],end="")
    print()
    t-=1
