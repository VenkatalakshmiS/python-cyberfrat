l1=[1,2,3,4]
print(l1)
l1=[1,2,3]
print(l1)

#map=input("Enter a number")
#print(type(map))

#map=tuple(map)
#print(type(map))

woman=('8','march')
print(type(woman))

woman2='8','march'
print(type(woman2))

woman3='8' 'march'
print(type(woman3))

x1=("deepa",'20',[8,'march'])
print(type(x1))

print(x1[2])
print(x1[2][1])
print(type(x1[2]))
print(type(x1[2][1]))

x1[2][0]=9
print(x1)

import itertools
import math
print(math.factorial(500))
print(math.factorial(3))

l1=[1,2,3]
ans=itertools.permutations(l1)
print(ans)

for element in ans:
    print(element)

#l1=[]
#for i in range(3):
    #l1.append(tuple(input("Enter tuple:")))

#print(l1)

#tp=tuple(input("Enter tuple:").split(","))
#print(tp)
#print(type(tp))

#ans=input("Enter numbers:")
#print(type(ans))
#ans=ans.split(",")
#print(ans)
#print(type(ans))

#ans=tuple(ans)
#print(ans)
#print(type(ans))
#print(type(ans[4]))

ex=1,2,3,4,5
print(type(ex))

ex=input("Enter a tuple:")
print(type(ex))

#ex=ex.split(",")
ex=tuple(ex)
print(ex)

l1=['d',3,'c',4,'a',2,1,'b',3.7,2.8,9.4]
print(l1)

t1,t2,t3=[],[],[]
for i in l1:
    if isinstance(i,int):
        t1.append(i)
    elif isinstance(i,float):
        t1.append(i)
    elif isinstance(i,str):
        t2.append(i)

t1.sort()
t2.sort()
t3=t1+t2
print(t3)
#l1=t3.copy()
#del t1, t2, t3
#print(l1)
