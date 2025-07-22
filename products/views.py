from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from .models import Product
from .serializers import ProductSerializer,ProductCreateSerializer
from rest_framework import status



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
    

class updateProduct(APIView):

    def put(self, request):
        product_id = request.data.get('id')
        if not product_id:
            return Response({
                "status": False,
                "message": "Product ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({
                "status": False,
                "message": "Product not found"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Product updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "status": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class deleteProduct(APIView):
    def delete(self, request,id):
        product_id = id
        if not product_id:
            return Response({
                "status": False,
                "message": "Product ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return Response({
                "status": True,
                "message": "Product deleted successfully"
            }, status=status.HTTP_200_OK)
        
        except Product.DoesNotExist:
            return Response({
                "status": False,
                "message": "Product not found"
            }, status=status.HTTP_404_NOT_FOUND)  