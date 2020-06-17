n = int(input())
arr=[0]*(n+1)
temp = list(map(int,input().split(" ")))[:n]
for i in range(len(temp)):
    arr[temp[i]]=i
m = int(input())
queries=list(map(int,input().split(" ")))[:m]
ansA=0
ansB=0
for query in queries:
    ansA+=arr[query]+1
    ansB+=n-arr[query]
print(ansA,ansB)
