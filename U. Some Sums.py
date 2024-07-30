x,y,z=map(int,input().split())   #3 number one line
sum_num=0
for i in range(1,x+1):
    sum_digit=sum(int(digit)for digit in str(i))    
    if y<=sum_digit<=z:
        sum_num+=i
print(sum_num)