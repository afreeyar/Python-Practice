from Practice4T import j
import os


x = 400
def myfunc(): 
    global x
    x=300
    print(x)
myfunc()
def myfunc2(): 
    x=600
    print(x)
myfunc2()
print(x)
x=500
print(x)


def myfunc():
    x=500
    def myfunc2():
        x=300
        def myfunc3():
            nonlocal x
            x=400
            print(x)
        myfunc3()
        print(x)
    myfunc2()
    print(x)
myfunc()


def myfunc():
    x=500
    def myfunc2():
        nonlocal x
        x=300
        def myfunc3():
            nonlocal x
            x=400
            print(x)
        myfunc3()
        print(x)
    myfunc2()
    print(x)
myfunc()


import platform
x = platform.system()
print(x)

print(j)
print (type(j))

import datetime

x = datetime.datetime.now()
print(x)


x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))


x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))


import math


x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

a = int(-7.25 * 2)
x = abs(float(a))
print(x)


x = pow(4, 3)
print(x)


x = math.sqrt(64)
print(x)


x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)

import json 


x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y = json.dumps(x)
print(y)


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=2))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=2, separators=(". ", " = ")))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4, sort_keys=True))


import re


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)


txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2 )
print(x)


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


try:
  f = open("Practice4D.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 


x = -1
try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as e:
    print(e)

x = "hello"
try:
  if not type(x) is int:
    raise TypeError("Only integers are allowed")
except Exception as e:
  print(e)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))


f = open("Practice4D.txt", "a")
f.write(" Now the file has more content!")
f.close()
f = open("Practice4D.txt", "r")
print(f.read())


f = open("Practice4D.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("Practice4D.txt", "r")
print(f.read())


os.remove("Practice4D.txt")
f = open("Practice4D.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("Practice4D.txt", "r")
print(f.read())


current_path = os.getcwd()
print(current_path)

