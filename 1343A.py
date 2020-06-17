import math
t=int(input())
while(t!=0):
    n=int(input())
    k=1
    while(True):
        k+=1
        deno=math.pow(2,k)-1
        if(n%deno!=0):
            continue
        x=n//deno
        break
    print(int(x))
    t-=1
