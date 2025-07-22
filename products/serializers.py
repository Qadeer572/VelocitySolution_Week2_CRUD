from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductCreateSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    description=serializers.CharField()
    price=serializers.DecimalField(max_digits=10, decimal_places=2)
    stock=serializers.IntegerField()
    

    