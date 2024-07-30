s=input()
line=int(input())
number=list(map(int,input().split()))

for num in number:
    for i in range(1,num+1):
        print(s,end='')
    print( )