from features.models import User, Brand, Cart, Category, SubCategory, Order, Payment, Product, Rating
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        max_length=200,
        min_length=4,
        validators=[UniqueValidator(
            queryset=User.objects.all(), message='email is already taken',)]

    )

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True,
        validators=[validate_password])

    class Meta:
        model = User
        fields = ('password', 'email', 'first_name', 'last_name', 'id')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
