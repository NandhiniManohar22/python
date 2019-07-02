 n1,n2=map(int,input().split())
 for num in range(n1,n2):
    length=len(str(num))
    sum=0
    temp=num
    while(temp>0):
       sum=sum+((temp%10)**length)
       temp=temp//10
    if sum==num:
       print(num,end=" ")
