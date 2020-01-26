n,m = input().split(" ")
n = int(n)
m = int(m)
quants = list(map(int,input().split(" ")))[:m]
quants.sort(reverse=False)
least = quants[n-1]-quants[0]
for i in range(m-n+1):
    if(quants[i+n-1] - quants[i] < least):
        least = quants[i+n-1] - quants[i]
print(least)