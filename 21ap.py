#ArithmaticProgression
v=input().split()
n=int(v[0])
a=int(v[1])
d=int(v[2])
def sumofAP( a, d,n) : 
    sum = 0
    i = 0
    while i < n : 
        sum = sum + a 
        a = a + d 
        i = i + 1
    return sum
print (sumofAP(a, d, n))
