# l1=['print','input','while','for','def']
# value=input("Enter the word:")
# for element in l1:
#     if element==value:
#         print("Keyword")
#         break

# if value in l1:
#     print("Keyword")
# else:
#     print("Not a keyword")

val = int(input("Enter value:"))
def magic(val):
    return val*10

ans=magic(val)
print(ans)

print(magic)
print(magic(val))

def magic(x,y):
    print(x*y)

magic(11,5)

magic=lambda x,y:x*y
print(magic(2,8))

l1=[2,92,27,67,37,16]
heriferi=lambda x:x.sort()
heriferi(l1)
print(l1)

name="deepa"
print("{}{}{}".format("$",name[::-1],"$"))

for i in range(4):
    for j in range(4):
        print("*")

x=10
if x>5:
    if x%2==0:
        if x==10:
            print("Yes it is 10")
        else:
            print("No, not 10")
    else:
        print("odd")
else:
    print("less than 5")

def magic():
    def inner():
        print("Hello")
    return inner

shortcut=magic()
print(shortcut)
shortcut()

l1=[]
for i in range(5):
    l1.append(1,2,3,4,5,6)

def magic(l1):
    for element in l1:
        if element%2!=0:
            l1.remove(element)
    print(l1)

print(magic(l1))
ans=l1.sort()
print(ans)

