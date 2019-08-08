n=input()
m,s=0,0
for c in n:
  if c.isalpha(): m+=1
  if c.isdigit(): s+=1
if m and s:
  print("Yes")
else:
  print("No")
