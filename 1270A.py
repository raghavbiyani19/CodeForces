X=lambda:input().split(" ")[:]
n = int(input())
list2=[]
mylist2=[]
for i in range(n):
    list1=[]
    list2=[]
    list1 = X()
    temp1=list(map(int,input().split(" ")))[:int(list1[1])]
    temp2=list(map(int,input().split(" ")))[:int(list1[2])]
    list2.append(temp1)
    list2.append(temp2)
    mylist2.append(list2)
 
for i in range(n):
    if(max(mylist2[i][0]) > max(mylist2[i][1])):
        print("YES")
    elif(max(mylist2[i][0]) == max(mylist2[i][1])):
        if(len(mylist2[i][0]) > len(mylist2[i][1])):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
