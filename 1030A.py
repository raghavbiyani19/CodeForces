n = int(input())
answers = list(map(int,input().split(" ")))[:n]
flag = 0
for item in answers:
    if item==1:
        flag = 1;
if flag == 1:
    print("HARD")
else:
    print("EASY")