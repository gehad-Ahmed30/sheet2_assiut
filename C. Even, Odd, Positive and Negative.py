num_value=int(input())
number=input()

numbers=list(map(int,number.split()))

flag_even=0
flag_odd=0
flag_positive=0
flag_negative=0

for i in numbers:
    if i%2==0:
        flag_even+=1
        
    else:
        flag_odd+=1
        
    if i>0:
        flag_positive+=1
        
    elif i<0:
        flag_negative+=1
        

print(f"Even: {flag_even}")
print(f"Odd: {flag_odd}")
print(f"Positive: {flag_positive}")
print(f"Negative: {flag_negative}")