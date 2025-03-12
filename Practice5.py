# Decorators

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Good Bye")
    return mfx


def greet2(j):
    def mfx(*args, **kwargs):
        a = int(input("Enter digit one: "))
        b = int(input("Enter digit two: "))
        j(a, b) 
    return mfx


@greet
def hello():
    print("Hello World")


@greet2
def add(a, b):
    print(a + b)


hello()
add()


#constructor
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5000)
for number in counter:
    print(number)


#marshamllow

from marshmallow import Schema, fields, post_load


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"


user_schema = UserSchema()


user = User(id=1, username="johndoe", email="johndoe@example.com")
user_data = user_schema.dump(user)
print(user_data)


user_input = {'id': 2, 'username': 'janedoe', 'email': 'janedoe@example.com'}
user_obj = user_schema.load(user_input)
print(user_obj) 


