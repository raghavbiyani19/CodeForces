n, d = map(int, input().split())
di = []
for _ in range(n):
	m, f = map(int, input().split())
	di.append([m, f])
 
di.sort(key=lambda x:x[0])
# print(di)
i = j = 0
ans = 0
s = 0
while j<n:
	if di[j][0]-di[i][0]<d:
		s += di[j][1]
		j += 1
		ans = max(ans,s)
	else:
		s -= di[i][1]
		i += 1
print(ans)
