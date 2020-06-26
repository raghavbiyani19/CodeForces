n=int(input())
arr=list(map(int,input().split()))[:n]
modifiedArr=sorted(list(set(arr)))
n=len(modifiedArr)
if n==1:
    print(0)
elif n==2:
    d=modifiedArr[1]-modifiedArr[0]
    if d & 1:
        print(d)
    else:
        print(d//2)
elif n==3:
    if modifiedArr[2]-modifiedArr[1] == modifiedArr[1]-modifiedArr[0]:
        print(modifiedArr[2]-modifiedArr[1])
    else:
        print(-1)
else:
    print(-1)
