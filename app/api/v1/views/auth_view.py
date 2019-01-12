from flask import jsonify,request,abort,make_response
from app.api.v1 import vers1 as v1
from app.api.v1.utils.validator import inputs_validate,hash_password
from app.api.v1.models.auth_model import member,users
from flask_jwt import jwt
import datetime
from app import create_app


inputs_validate = inputs_validate()


#sign up endpoint
@v1.route('/signup', methods=['POST'])
def register():

    # Check for json data
    data = request.get_json()
    if not data:
        return jsonify({"status": 400, "message": "POST of type Application/JSON expected"}), 400

    # Check for empty inputs
    if not all(field in data for field in ["firstname", "lastname", "othername", "email", "phoneNumber", "username", "password", "cpassword" ]):
        return jsonify({"status": 400, "message": "All fields are required"}), 400 

    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    email = data['email']
    phoneNumber = data['phoneNumber']
    username = data['username']
    password = data['password']
    cpassword = data['cpassword']

    #validate email
    if not inputs_validate.email_validation(email):
        return jsonify({"status": 400, "message": "Your email is not valid"}), 400

    #validate password
    if not inputs_validate.password_validation(password):
        return jsonify({"status": 400, "message": "Your password is not valid"}), 400

    if not inputs_validate.compare_password(password, cpassword):
        return jsonify({"status": 400, "message": "Passwords do not match"}), 400

    exists_usr = member().user_exists(email)
    if exists_usr:
        return jsonify({"status": 400, "message": "email is already registered,please use a different email or login"}), 400

    pwd = hash_password(password) #encrypt the password
    user = member(firstname,lastname,othername,email,phoneNumber,username,pwd).add_user() #append registered user
    return jsonify(user), 201
    

#sign in endpoint
@v1.route('/signin', methods=['POST'])
def login():
    # Check for json data
    data = request.get_json()
    if not data:
        return jsonify({"status": 400, "message": "POST of type Application/JSON expected"}), 400

    # Check for empty inputs
    if not all(field in data for field in ["email","password"]):
        return jsonify({"status": 400, "message": "All fields are required"}), 400 

    email = data['email']
    password = data['password']

    #validate email
    if not inputs_validate.email_validation(email):
        return jsonify({"status": 400, "message": "Your email is not valid"}), 400

    #check if email exists
    usr = member().user_exists(email)
    if not usr:
        abort(make_response(jsonify({"message":"User not Found"}),404))

    #Check if password match
    if not inputs_validate.compare_password(usr['password'],password):
        abort(make_response(jsonify({'message':'Invalid Password'}),400))

    