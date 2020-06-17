n = int(input())
nums=list(map(int,input().split()))[:n]
total=sum(nums)
count=0
for i in range(1,6):
    if((i+total)%(n+1)!=1):
        count+=1
print(count)
