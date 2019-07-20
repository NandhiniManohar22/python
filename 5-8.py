nan=int(input())
nan1=list(map(int,input().split()))
temp=0
div=len(nan1)
for i in range(nan):
   temp+=nan1[i]
res=temp//div
print(res)
   
