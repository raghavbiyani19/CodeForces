def solve(n):
    if n==1 or n==2:
        print(-1)
    elif n & 1:
        tmp=n**2
        print(tmp//2, tmp//2 +1)
    else:
        tmp=(n//2)**2
        print(tmp-1, tmp+1)

n=int(input())
solve(n)
