length = list(map(int,input().split(" ")))[:4]
length.sort()
if (length[0] + length[1] > length[2] or length[1] + length[2] > length[3]):
    print("TRIANGLE")
elif (length[0] + length[1] == length[2] or length[1] + length[2] == length[3]):
    print("SEGMENT")
else:    
    print("IMPOSSIBLE")