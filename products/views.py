from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from .models import Product
from .serializers import ProductSerializer,ProductCreateSerializer



class productsList(APIView):
     
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        if not products:
            return Response({
                "status": False,
                "message": "No products found",
                "data": []
            })
        
        return Response({
            "status": True,
            "message": "Products retrieved successfully",
            "data": serializer.data
        })


class addProduct(APIView):

    def post(self,request):  
        serializer=ProductCreateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": "Invalid data",
                "errors": serializer.errors
            }, status=400)    

        product= Product.objects.create(
            name=serializer.validated_data['name'],
            description=serializer.validated_data['description'],
            price=serializer.validated_data['price'],
            stock=serializer.validated_data['stock']
        )

        product.save()
        
        return Response({
            "status": True,
            "message": "Product created successfully",
            "data": ProductSerializer(product).data
        }, status=201)   