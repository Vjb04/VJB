#Multiply
a=int(input())
list=[]
for i in range(1,6):
	mul=a*i
	list.append(mul)
print(" ".join(map(str,list)))
