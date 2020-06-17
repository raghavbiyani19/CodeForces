t=int(input())
while(t!=0):
    n,a,b=map(int,input().split())
    aIndex=a
    for i in range(n):
        print(chr(ord('a')+(i%b)),end="")
    print()
    t-=1
