l1=[1,2,3,4,5]
print(l1)

l1=[1,2,3,"Python"]
print(l1)

l1.append(34)
print(l1)

l1.insert(3,"Deepa")
print(l1)

l1.insert(2,"Venkat")
print(l1)

element="Deepa"
print(type(element))

num=5
print(type(num))

l1.insert(3,element)
print(l1)
print(l1[2])

n1=10
n2=20
n1,n2=n2,n1
print(n1)
print(n2)

n1=10
n2=20
n3=30
n4=40
n1,n2,n3,n4=n4,n3,n2,n1
print(n1,n2,n3,n4)

s1=set(l1)
print(s1)

l1=[1,2,3,4,5]
print(l1.pop())

l1=[1,2,3,"Python"]
print(l1.pop())
print(l1)

l1=[34,12,78,"Python","deepa"]
l1.remove(78)
print(l1)

val=l1[3]
l1.remove(val)
print(l1)

l1=[34,12,78,"Python","deepa"]
for element in l1:
    if element==78:
        l1.remove(element)
print(l1)


l1=[1,2,3,4,5]
l2=l1
print(l1.pop())
print(l1)
print(l2)

l1=[1,2,3,4,5,6,7]
#l2=l1.copy
#print(l1)
#print(l2)

#l2=l1.copy()
#print(l2)
print(l1.pop())

l1=l2[0:2]
print(l1)


l2=['a','b','c']
l1.extend(l2)
print(l1)

l1.insert(0,l2)
print(l1)

l1=l1[0:-2]
print(l1)

alpha=['b','q','a','t']
alpha.sort()
print(alpha)

num=[345,7,32,7464,868]
num.sort()
print(num)

#num.clear()
#print(num)

#del alpha
#print(alpha)

l1=[1,2,3,4,5,6,7,8]
l2=[x for x in l1]
print(l2)

l2=[x for x in l1 if x%2!=0]
print(l2)

l2=[x if x%2!=0 else 'even' for x in l1]
print(l2)

num=[x for x in range(0,101)]
print(num)

l2=[x for x in num if x%2==0]
print(l2)
