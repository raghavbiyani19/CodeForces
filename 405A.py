n = int(input())
blocks = list(map(int,input().split(" ")))[:n]
blocks.sort(reverse=False)
print(*blocks,sep=' ')