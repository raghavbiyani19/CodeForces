n = int(input())
Forces = []
for i in range(n):
    Forces.append(list(map(int,input().split(" ")))[:3])
xSum = 0
ySum = 0
zSum = 0
for i in range(n):
    xSum += Forces[i][0]
    ySum += Forces[i][1]
    zSum += Forces[i][2]
if(xSum == 0 and ySum == 0 and zSum == 0):
    print("YES")
else:
    print("NO")