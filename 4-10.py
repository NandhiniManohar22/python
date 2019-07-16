nan=int(input())
m,s=0,1
while nan>0:
   print(s,end=' ')
   m,s=s,m+s
   nan=nan-1
