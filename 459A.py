x1,y1,x2,y2 = map(int,input().split(" "))
xDiff = x2-x1
yDiff = y2-y1
if xDiff != 0 and yDiff!=0:
    x3=x1
    x4=x2
    y3=y2
    y4=y1
elif xDiff!=0:
    x3=x1
    x4=x2
    y3=y1+xDiff
    y4=y2+xDiff
else:
    x3=x1+yDiff
    x4=x2+yDiff
    y3=y1
    y4=y2
if (xDiff != 0 and yDiff != 0 and abs(xDiff) != abs(yDiff)):
    print(-1)
else:
    print(x3,y3,x4,y4)