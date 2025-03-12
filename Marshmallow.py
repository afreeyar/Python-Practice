from marshmallow import Schema, fields, post_load


class AddressSchema(Schema):
    street = fields.Str()
    city = fields.Str()
class PersonSchema(Schema):
    name = fields.Str()
    address = fields.Nested(AddressSchema)


person = {"name": "John", "address": {"street": "123 Main St", "city": "Springfield"}}
person_schema = PersonSchema()
person_json = person_schema.dump(person)
print(person_json)




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name} is {self.age} years old."
class PersonInfoSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    @post_load
    def create_person(self, data, **kwargs):
        return Person(**data)


input_data = {}
input_data["name"] = input("What is your name? ")
input_data["age"] = int(input("What is your age? "))
schema = PersonInfoSchema()
person = schema.load(input_data)
result = schema.dump(person)
print(result)
