n1=int(input())
n2=list(map(int,input().split()))
n2.sort()
for i in n2:
  print(i,end=" ")
