def sign(num):
    if(num>0):
        return 1
    else:
        return 0

t=int(input())
while(t!=0):
    n=int(input())
    arr=list(map(int,input().split()))[:n]
    ans=0
    i=0
    while(i<n):
        #print("FROM I=",i)
        j=i+1
        maxNum=arr[i]
        while(j<n and sign(arr[i])==sign(arr[j])):
            maxNum=max(maxNum,arr[j])
            j+=1
        ans+=maxNum
        #print("SELECTED",maxNum)
        #print("J=",j)
        i=j-1
        #print("I = ",i)
        i+=1
    print(ans)
    t-=1
