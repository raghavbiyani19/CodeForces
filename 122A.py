numList=[]
n = int(input())
for i in range(1,n+1):
    flag = 1;
    i = str(i)
    for j in range(len(i)):
        if (i[j] not in ['4','7']):
            flag = 0;
    if(flag==1):
        numList.append(int(i))
flag = 0
for item in numList:
    if(n%item==0):
        flag = 1
        break
if(flag == 1):
    print('YES')
else:
    print('NO')