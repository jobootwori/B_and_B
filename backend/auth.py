from flask import Flask,jsonify, request, make_response
from flask_restx import Resource,Namespace,fields
from models import Image_Upload, User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import (JWTManager,
create_access_token,create_refresh_token,
get_jwt_identity,
jwt_required)

auth_ns = Namespace('auth',description="A namespace for authentication")

#model (serializer)
signUp_model = auth_ns.model(
    "SignUp",
    {
        "username":fields.String(),
        "email":fields.String(),
        "password":fields.String()
    }
)

logIn_model = auth_ns.model(
    "LogIn",
    {
    "username":fields.String(),
    "password":fields.String()
    }
)

@auth_ns.route('/signup')
class signUp(Resource):
    """sign up user"""

    @auth_ns.expect(signUp_model)
    def post(self):
        data=request.get_json()

        username = data.get("username")
        db_user = User.query.filter_by(username=username).first()

        if db_user is not None:
            return jsonify({"message": f"User with username {username} already exists"})

        new_user=User(
            username=data.get('username'),
            email=data.get('email'),
            password=generate_password_hash(data.get('password'))

        )

        new_user.save()

        return make_response(jsonify({"message":"User created successfully"}),201)
    
@auth_ns.route('/image_upload')
class uploadImage(Resource):
    """Upload Rental images"""

    @auth_ns.expect(Image_Upload)
    def post(self):


        filename = request.files['filename']
        image = request.files['image'].read()
        new_image = Image_Upload(filename=filename, image=image)
        new_image.save()
        return make_response(jsonify({'message': 'Image uploaded successfully!'}),201)
    
@auth_ns.route('/login')
class logIn(Resource):
    """Log in as user"""

    @auth_ns.expect(logIn_model)
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        db_user = User.query.filter_by(username=username).first()

        if  db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity = db_user.username)
            refresh_token = create_refresh_token(identity = db_user.username)

        return jsonify(
            {"access_token": access_token, "refresh_token": refresh_token}
        )
    
@auth_ns.route('/refresh')
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):

        current_user=get_jwt_identity()

        new_access_token=create_access_token(identity=current_user)

        return make_response(jsonify({"access_token":new_access_token}),200)
