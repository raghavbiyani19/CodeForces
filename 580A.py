n = int(input())
maxCount=1
count=1
profits = list(map(int,input().split(" ")))[:n]
for i in range(n):
    if(i>0):
        if(profits[i]>=profits[i-1]):
            count+=1
            maxCount=max(maxCount,count)
        else:
            count=1
print(maxCount)