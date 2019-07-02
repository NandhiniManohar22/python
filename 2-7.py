N=int(input())
length=len(str(N))
sum=0
temp=N
while(temp!=0) and (N<=100000):
   sum=sum+((temp%10)**length)
   temp=temp//10
if sum==N:
    print("yes")
else:
    print("no")
