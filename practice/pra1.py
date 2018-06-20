a=input().rstrip().split(' ')
for i in range(9):
    print(int(a[0])+int(a[1])*i,end=' ')
print(int(a[0])+int(a[1])*9)
