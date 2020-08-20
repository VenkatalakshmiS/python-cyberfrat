val=int(input("Enter value:"))
def magic(val):
    return val/3
ans=magic(val)
print(ans)



def magic(*args):
    for arg in args:
        print(arg)

magic("Cyberfrat","Python","session")



def magic(arg1,*args):
    print("First argument",arg1)
    for arg in args:
        print("Next argument",arg)

magic("20","August","2020")



def magic(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

magic(name="Deepa",age="22")



def magic(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)
args=("stay","safe","everyone")
magic(*args)



kwargs={"arg1":"cyberfrat","arg2":"python","arg3":"session"}
magic(**kwargs)



def cube(x):
    return x*x*x
result=cube(10)
print(result)

cube_val=cube
result=cube_val(3)
print(result)



def cube(x):
    return(x*x*x)
def my_cube(method,arg_list):
    result=list()
    for item in arg_list:
        result.append(method(item))
    return result

my_list=my_cube(cube,[1,2,3,4,5,6,7,8])
print(my_list)


def magic():
    x=100
    print(x)
magic()


def red():
    a=1
    def blue():
        b=2
        print(a)
        print(b)
    blue()
    print(a)

red()



x=100
def magic():
    print(x)

magic()



x=300
def magic():
    x=200
    print(x)
magic()
print(x)



def magic():
    global x
    x=300
magic()
print(x)


x=300
def magic():
    global x
    x=200
magic()
print(x)
