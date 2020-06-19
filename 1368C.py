def main():
    n=int(input())
    pairs=[]
    pairs.append([0,0])
    pairs.append([0,1])
    pairs.append([1,0])
    pairs.append([1,1])
    while(n):
        x=pairs[-1][0]
        y=pairs[-1][1]
        pairs.append([x+1,y])
        pairs.append([x,y+1])
        pairs.append([x+1,y+1])
        n-=1
    size=len(pairs)
    print(size)
    for i in range(size):
        print(pairs[i][0],pairs[i][1])
