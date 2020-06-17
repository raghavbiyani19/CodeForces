from collections import defaultdict
n, k = map(int,input().split())
a = list(map(int,input().split()))
freq = defaultdict(int)
d = defaultdict(int)
ans = 0
for i in range(n):
    if a[i]%k==0:
        ans+=d[a[i]//k]
        d[a[i]]+=freq[a[i]//k]
    freq[a[i]]+=1
print(ans)
