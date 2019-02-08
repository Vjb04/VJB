#EVEN

a=input().split()
n=int(a[0])
q=int(a[1])
list=[]
for i in range(n+1,q):
    if(i%2==0):
    	list.append(i)
print(" ".join(map(str,list)))
