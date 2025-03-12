class MyClass:
  x = 5
print(MyClass)


class MyClass:
    x = 5
print(MyClass.x) 


class MyClass:
    def __init__(test):
        test.x = 10  # Instance variable
    def function_a(test):
        test.x += 5
        print("Inside function_a:", test.x)
    def function_b(test):
        print("Inside function_b:", test.x)
obj = MyClass()
obj.function_a()
obj.function_b()


thisdict =	{
  "brand": ["Ford" , "Cars" , "life"],
  "model": "Mustang",
  "year": 1964
}
x = input("Key?")
print(thisdict[x][1])

