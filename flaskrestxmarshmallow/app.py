from flask import Flask
from flask_restx import Api, Resource, fields
from marshmallow import Schema, fields as ma_fields, validate, ValidationError, validates

app = Flask(__name__)
api = Api(app)

class AdminSchema(Schema):
    username = ma_fields.Str(
        required=True,
        validate=[
            validate.Length(min=1, max=50, error="Username must be between 1 and 50 characters"),
            validate.Regexp(
                regex=r'^[a-zA-Z0-9_-]+$',
                error="Username can only contain letters, numbers, underscores, and hyphens",
            ),
        ],
    )
    password = ma_fields.Str(
        required=True,
        validate=[
            validate.Length(min=8, max=100, error="Password must be between 8 and 100 characters"),
        ],
    )

    @validates('password')
    def validate_password(self, value):
        if not any(char.isnumeric() for char in value):
            raise ValidationError("Password must contain at least one numeric character")

        if not any(char.isupper() for char in value):
            raise ValidationError("Password must contain at least one uppercase letter")

        if not any(char.islower() for char in value):
            raise ValidationError("Password must contain at least one lowercase letter")

admin_schema = AdminSchema()
print(type(admin_schema))

admin_registration_model = api.model('AdminRegistration', {
    'username': fields.String(required=True, description='Admin username', **admin_schema.fields['username'].metadata),
    'password': fields.String(required=True, description='Admin password', **admin_schema.fields['password'].metadata)
})

print(type(admin_registration_model))

@api.route('/admin/register')
@api.expect(admin_registration_model)
class AdminRegistration(Resource):
    def post(self):
        try:
            data = admin_schema.load(api.payload)
        except ValidationError as err:
            return {"message": "Validation error", "errors": err.messages}, 400

        username = data['username']
        password = data['password']

        return {"message": "Registration successful", "username": username}, 201  
    
api.add_namespace(api)

if __name__ == '__main__':
    app.run(debug=True)
