import math
n = int(input())
nums = list(map(int,input().split(" ")))[:n]
x=nums[0]
for item in nums[1:]:
	x=math.gcd(x,item)
ans=0
for i in range(1, (int)(math.sqrt(x)) + 1):
    if(x%i == 0):
        if(x/i==i):
            ans+=1
        else:
            ans+=2
print(ans)