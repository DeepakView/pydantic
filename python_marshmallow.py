# from marshmallow import Schema, fields, validate

# class UserProfileSchema(Schema):
#     name = fields.String(required=True, validate=validate.Length(min=2, max=50))
#     age = fields.Integer(required=True, validate=validate.Range(min=18, max=100))
#     email = fields.Email(required=True)

# data = {"name": " ", "age": "25", "email": "deepakdeepak3300@gmail.com"}

# try:
#     user_profile = UserProfileSchema().load(data)
#     print(f"Marshmallow User Profile: {user_profile}")
# except Exception as e:
#     print(f"Marshmallow Error: {e}")


from marshmallow import Schema, fields, validate, ValidationError

class UserSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=4, max=20))
    age = fields.Integer(required=True, validate=validate.Range(min=18))

data = {"username": "Deepak", "age":15}

try:
    user = UserSchema().load(data)
    print(f"Marshmallow User: {user}")
except Exception as e:
    print(f"Marshmallow Error: {e.messages}")









