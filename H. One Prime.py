number=int(input())
flag=True
for i in range(2,int(number/2)): # loop prime
    if number%i==0:     #number/prime
        flag=False
if flag:
    print("YES")
else:
    print("NO")


