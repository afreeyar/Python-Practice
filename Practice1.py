print ("hello World")


import sys
print(sys.version)


if 5 > 2:
    print("5 is greater then 2")
if 2 < 5:
    print("2 is smaller then 5")


a=5 
b="Hello world"
if a > 2:
    print(b)
print(type(b),b)


c, d, e = "Hello", "World", "!"
print( c )
print( d )
print( e )
print ( c , d + e)


f= int(input(" First digit: \n"))
g= input(" Function to use: \n")
h= int(input(" Second Digit: \n"))
def i():
    if g=="*" :
        i = f * h
        print( f, g, h, "=" , i)
    elif g=="+" :
        i = f + h
        print( f, g, h, "=" , i)
    elif g=="-" :
        i = f - h
        print( f, g, h, "=" , i)
    elif g=="/" :
        i = f / h
        print( f, g, h, "=" , i)
    else:
       print("Error!", "Wrong function Defined.")
i()


import random
def j():
    global j
    j=(random.randrange(1,10))
    print(j)
j()
print(type(j))


k = ("Hello, World!","high","low")
print(k[0])
print(k[1])
print(k[2])


l=int(input("Value"))
while l <= 10:
    print("Hello World")
    l +=1


m="Hello World"
n=len(m)
print(len(m), n)


c=("Hi how are you ")
if "Hi" in c:
    print("No")
print("Hi how are you" in c)
print("Hi how are you" not in c)


b = "Hello, World!"
print(b[-5:-2])


a = "Hello, World . How , DO . You , DO."
b = a.split( ".")
print(b)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}


x = car.keys()
print(x) 
car["color"] = "white"
print(x) 
