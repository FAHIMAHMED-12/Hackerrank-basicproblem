n=int(input())
original=n
sum=0
a=len(str(n))
while(n>0):
    digit= n%10
    sum=sum+digit**a
    n=n//10
if (original==sum):
    print("Armstrong")
else: 
    print("Not armstrong")


    