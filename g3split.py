n=input().split()
a=int(n[0])
b=int(n[1])
c=int(n[2])
if(a>b and a>c):
  print(a)
elif(b>a and b>c):
  print(b)
elif(c>a and c>b):
  print(c)
else:
  print("Invalid")
