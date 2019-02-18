#LongestCommonPrefix
list=[]
a=int(input())
d=0
for i in range(0,a):
  b=input()
  list=b
while a>0:
  print(b[d],end="")
  d=d+1
  a=a-1
