from django.shortcuts import render
from .serializers import registerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
#from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import person_collection
 


 
        
def login_View(request):
        return render(request, 'users/login.html')

def register_View(request):
        return render(request, 'users/signup.html')

class register_api(APIView):
        
        def post(self,request):
                serializer = registerSerializer(data=request.data)
                if serializer.is_valid():
                    email = serializer.validated_data['email']
                    first_name = serializer.validated_data['firstName']
                    last_name = serializer.validated_data['lastName']
                    password = serializer.validated_data['password']
                    
                    # Create the user
                    record = {
                        "username":email, 
                        "email":email, 
                        "first_name":first_name, 
                        "last_name":last_name, 
                        "password":password
                    }

                    person_collection.insert_one(record)
                    
                    
                    return Response({"message": "User created successfully"}, status=201)
                return Response(serializer.errors, status=400)