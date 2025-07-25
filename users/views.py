from django.shortcuts import render
from .serializers import registerSerializer,loginSerilaizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
#from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import person_collection
import bcrypt
import jwt
import datetime
from VelocitySolution_Week2_CRUD.settings import SECRET_KEY
from rest_framework.permissions import IsAuthenticated



 
        
def login_View(request):
        return render(request, 'users/login.html')

def register_View(request):
        return render(request, 'users/signup.html')

def dashboard_view(request):
        return render(request, 'users/dashboard.html')
      
class register_api(APIView):
        
        def post(self,request):
                serializer = registerSerializer(data=request.data)
                if serializer.is_valid():
                    email = serializer.validated_data['email']

                    if person_collection.find_one({"email": email}):
                        return Response({
                              "status" : False,
                              "error": "Email already exists"
                              }, status=400)
                    
                    first_name = serializer.validated_data['firstName']
                    last_name = serializer.validated_data['lastName']
                    password = serializer.validated_data['password']


                    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

                    
                    record = {
                        "username":email, 
                        "email":email, 
                        "first_name":first_name, 
                        "last_name":last_name, 
                        "password":hashed
                    }

                    person_collection.insert_one(record)
                    
                    
                    return Response({
                           "status": True,
                           "message": "User created successfully"
                          }, status=201)
                return Response({
                      "status": False,
                      "error":serializer.errors}
                      , status=400)


 

class login_api(APIView):
    def post(self, request):
        serializer = loginSerilaizer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = person_collection.find_one({"email": email})

            if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
                # Generate JWT token
                payload = {
                    "email": email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

                return Response({
                      "status": True,
                      "message": "Login successful",
                      "token": token
                      }, status=200)

            return Response({
                  "status": False,
                  "error": "User Not Register or Invalid Credentials"
                  }, status=400)

        return Response({
             "status": False,
              "errors":serializer.errors
              }, status=400)


class contact(APIView):
      permission_classes=[IsAuthenticated]

      def get(self,request):
            users= person_collection.find()
            return Response({
                "status": True,
                "data": list(users)
            })
