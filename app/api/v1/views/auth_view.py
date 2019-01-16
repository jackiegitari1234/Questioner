# global builtin modules
import datetime
import os

#downloaded modules
from flask import jsonify,request,abort,make_response,json

#local imports
from app.api.v1 import vers1 as v1
from app.api.v1.utils.validator import inputs_validate,hash_password
from app.api.v1.models.auth_model import add_user,users,token,user_exists


SECRET_KEY = os.getenv("SECRET")


inputs_validate = inputs_validate()


#sign up endpoint
@v1.route('/signup', methods=['POST'])
def register():

    # Check for json data
    data = request.get_json()
    if not data:
        abort(make_response(jsonify({"message":"POST of type Application/JSON expected"}),400))

    # Check for empty inputs
    if not all(field in data for field in ["firstname", "lastname", "othername", "email", "phoneNumber", "username", "password", "cpassword" ]):
        abort(make_response(jsonify({"message":"All fields are required"}),400))

    if len (data) > 8:
        abort(make_response(jsonify({"message":"Please provide just the required fields"}),400))

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
        abort(make_response(jsonify({"message":"Your email is not valid"}),400))

    #validate password
    if not inputs_validate.password_validation(password):
        abort(make_response(jsonify({"message":"Your password is not valid"}),400))

    if not inputs_validate.compare_password(password, cpassword):
        abort(make_response(jsonify({"message":"Passwords do not match"}),400))

    exists_usr = user_exists(email)
    if exists_usr:
        abort(make_response(jsonify({"message":"email is already registered,please use a different email or login"}),400))

    pwd = hash_password(password) #encrypt the password
    user = add_user(firstname,lastname,othername,email,phoneNumber,username,pwd) #append registered user
    abort(make_response(jsonify(user),201))
    

#sign in endpoint
@v1.route('/signin', methods=['POST'])
def login():

    data = request.get_json()
    if not data:
        abort(make_response(jsonify({"message":"POST of type Application/JSON expected"}),400))
        

    # Check for empty inputs
    if not all(field in data for field in ["email","password"]):
        abort(make_response(jsonify({"message":"Email and Paswword are required"}),400))

    if len (data) > 2:
        abort(make_response(jsonify({"message":"Please provide just email and password"}),400))

    email = data['email']
    password = data['password']


    #validate email
    if not inputs_validate.email_validation(email):
        abort(make_response(jsonify({"message":"Please enter a valid email"}),400))

    #check if email exists
    usr = user_exists(email)
    if not usr:
        abort(make_response(jsonify({"message":"User not Found"}),404))

    #Check if password match
    if not inputs_validate.check_password(usr['password'],password):
        abort(make_response(jsonify({'message':'Input contained a wrong Password'}),400)) 

    else: 
        abort(make_response(jsonify({'message':'user sucessfully logged in'}),400)) 
    