n=input()
m1=0
for i in range(len(n)):
    if (n[i].isalpha() or n[i].isnumeric() or n[i]==" "):
      continue
    m1=m1+1
else:
    print(m1)
   
