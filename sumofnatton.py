n=int(input('Enter a number: \n'))
if(n<0):
	print('Please Enter a positive number')
else:
	sum=0
	while(n>0):
		sum+=n
		n-=1
	print(sum)
