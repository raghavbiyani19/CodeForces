#B-Mafia
import math
n=int(input())
l=list(map(int,input().split()))
m=max(l)
print(max(m,math.ceil(sum(l)/(n-1))))
