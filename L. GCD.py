number=input()
x,y=map(int,number.split())
z=min(x,y)
result=1
for i in range(1,z+1):
    if x%i==0 and y%i==0:
        result=i
print(result)
