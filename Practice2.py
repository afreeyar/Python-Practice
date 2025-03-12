a= {
  "Name": "Afrand",
  "Year": "2002",
  "Age": "22",
  "Birthday": "27 January",
  "Height": "6'0",
}
for x, y in a.items():
  print(x, y)


b = {
  "Friend1" : {
    "Name" : "Owais",
    "year" : 1999
  },
  "Friend2" : {
    "name" : "Saqin",
    "year" : 2001
  },
  "Friend3" : {
    "name" : "Afrand",
    "year" : 2002
  }
}
print(b)


Owais = {
  "name" : "Owais",
  "year" : 1999
}
Saqib = {
  "name" : "Saqub",
  "year" : 2001
}
Afrand = {
  "name" : "Afrand",
  "year" : 2002
}
c = {
  "Friend1" : Owais,
  "Friend2" : Saqib,
  "Friend3" : Afrand
}
print(c)


d = {
  "Friend1" : {
    "name" : "Owais",
    "year" : 1999
  },
  "Friend2" : {
    "name" : "Saqib",
    "year" : 2001
  },
  "Friend3" : {
    "name" : "Afrand",
    "year" : 2002
  }
}
for x, obj in d.items():
    print(x) 
    for y in obj:
        print(y + ':', obj[y])


def e(*friends):
  for friend in friends:
    print("The friends are " + friend)
e("Owais", "Saqib", "Afrand")


def f(**friend):
  print("Best friend is " + friend["name2"])
f(name1 = "Owais", name2 = "Saqib")


def g(h):
  if(h > 0):
    result = h + g(h - 1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results:")
g(6)


i = lambda j, k, l: j + k + l
print(i(20, 21, 22))


def m(n):
  return lambda o : o * n
q=int(input("Add a value: \n"))
r=int(input("Add a value: \n"))
p = m(q)
print(" The multiplication of the value is:", p(r))


class s:
  def __init__(self, name, age):
    self.name = name
    self.age = age
t = s("Afrand", 22)
print(t.name)
print(t.age)


class t:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"    
t = t("Afrand", 22)
print(t)


class u:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"    
p = u("Afrand", 22)
print(p)


class q:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
r = q("Afrand", 22)
r.myfunc()


class s:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def t(self):
    print(self.firstname, self.lastname)
u = s("Afrand", "Yar")
u.t()


class v:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def w(self):
    print(self.firstname, self.lastname)
class x(v):
  pass
y = x("Afrand", "Yar")
y.w()


class z:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def aa(self):
    print(self.firstname, self.lastname)
class ab(z):
  def __init__(self, fname, lname):
    z.__init__(self, fname, lname)
ac = ab("Afrand", "Yar")
ac.aa()


class ad:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def ae(self):
    print(self.firstname, self.lastname)
class af(ad):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
ag = af("Afrand", "Yar", 2019)
print(ag.graduationyear)


class ah:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def ai(self):
    print(self.firstname, self.lastname)
class aj(ah):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def ak(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
al = aj("Afrand", "Yar", 2024)
al.ak()
