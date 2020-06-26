matrix=[]
flag=0
for i in range(5):
    matrix.append(list(map(int,input().split()))[:5])
for i in range(5):
    for j in range(5):
        if(matrix[i][j]==1):
            jVal=j
            iVal=i
            flag=1
            break
    if(flag==1):
        break
print(abs(iVal-2)+abs(jVal-2))
