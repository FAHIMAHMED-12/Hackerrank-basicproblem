n=int(input())
x1=0
x2=1
sum= 0
if n<=0:
    print("give greater than zero")
else:
    for i in range(0,n):
        print(sum, end=" ")
        x1=x2
        x2=sum
        sum=x1+x2