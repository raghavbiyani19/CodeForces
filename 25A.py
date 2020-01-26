n = int(input())
nums = list(map(int,input().split(" ")))
evens=[]
odds=[]
for item in nums:
    if(item%2==0):
        evens.append(item)
    else:
        odds.append(item)
if(len(odds) == 1):
    print(nums.index(odds[0])+1)
else:
    print(nums.index(evens[0])+1)