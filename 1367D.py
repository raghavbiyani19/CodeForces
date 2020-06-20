t=int(input())
while(t):
	s = list(input())
	x = sorted(set(s))
	m = int(input())
	b = list(map(int, input().split()))
	l=[-1]*m
	while(sum(b)!=(-m)):
		z=set()
		for i in range(m):
			if b[i]==0:
				z.add(i)
				b[i]=-1
		while True:
			q=x.pop()
			if len(z)<=s.count(q):
				for i in z:
					l[i]=q
				break
		for i in z:
			for k in range(m):
				if b[k] != -1:
					b[k] -= abs(i - k)
	print(*l,sep="")
	t-=1
