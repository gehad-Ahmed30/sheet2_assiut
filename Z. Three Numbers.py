number=input()
x,y =map(int,number.split())
sum_n=0
for i in range(x+1):
    for j in range(x+1):
        a=y-i-j

        if 0<= a <=x:
            sum_n+=1
print(sum_n)
