#prIME
n,q=input().split()
n=int(n)
q=int(q)
list=[]
for num in range(n+1,q):
	for d in range(2,num):
		if num%d==0:
			break
	else:
		list.append(num)
print(" ".join(map(str,list)))
#PRime
