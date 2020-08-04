for val in "string":
    if val=="i":
        continue
    print(val)
    print("The end")



for val in "string":
    if val=="i":
        continue
    print(val)

for val in "string":
    if val=="i":
        break
    print(val)


name="Python"
print(name)
print(name[0])
print(name[2])
print(name[0:3])
print(name[-1])
print(name[-6])
print(name[-1:0])
print(name[-6])
print(name[0:-3])
print(name[-1:-3])
print(name[-3:-1])

name="Python"
print(len(name))

for i in range(len(name)):
    print(i)

for i in range(len(name)):
    print(name[i])

name="this is python"
print(name.title())
print(name.upper())
print(name.lower())

fname,midname,lname=name.split(" ")
print(fname)
print(midname)
print(lname)

name="venkata lakshmi"
name=name.strip()
print(name)
name=name.lstrip()
print(name)
name=name.rstrip()
print(name)

session="Python Training"
for letter in session:
    print(letter)

for i in range(len(session)):
    print(session[i])

while(0):
    print("Hello")

name="Python"
print(name.find('P'))
print(name.find('o'))
print(name.find('hon'))
print(name.find('ubuntu'))


#print(help(str))
#print(help(str.join))

print(name.find('y'))

name="malayalam"
print(name.find('a'))
print(name.rfind('a'))

name="this is PYTHON"
print(name.swapcase())
print(name.zfill(25))
print(name.count('s'))
print(name[::-1])

print(chr(65))
print(chr(78))

name="Deepa"
for letter in name:
    print(ord(letter))

list=[65,78]
for num in list:
    print(chr(num))

name="deepa\n"
print(name)

for letter in name:
    print(ord(letter))
