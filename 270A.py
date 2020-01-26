n = int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))
 
for i in range(n):
    m = 360/(180-nums[i])
    if(m - int(m) == 0):
        print("YES")
    else:
        print("NO")