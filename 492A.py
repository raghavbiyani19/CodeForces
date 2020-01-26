n,l = input().split(" ")
n = int(n)
l = int(l)
positions = list(map(int,input().split(" ")))[:n]
positions.sort(reverse=False)
dist1 = positions[0]
dist = 0
dist2 = l - positions[n-1]
for i in range(n-1):
    if((positions[i+1]-positions[i]) > dist):
        dist = positions[i+1]-positions[i]
if(dist1 > dist/2 and dist1 > dist2):
    print(dist1)
elif(dist/2 > dist2):
    print(dist/2)
else:
    print(dist2)
