from django.contrib.auth import get_user_model
from features.models import Brand, Cart, Category, SubCategory, Order, Payment, Product, Rating
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
import json
import random
from rest_framework import permissions

from rest_framework.authtoken.models import Token

from rest_framework import viewsets
from rest_framework import status, generics
from rest_framework.views import APIView
from features.serializers.features_serializers import (
    UserSerializer,
    BrandSerializer,
    CartSerializer,
    CategorySerializer,
    SubCategorySerializer,
    OrderSerializer,
    PaymentSerializer,
    RatingSerializer,
    ProductSerializer)

User = get_user_model()


class UserApiView(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class BrandApiView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class CartApiView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def has_object_permission(self, request, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return obj.owner == request.user


class CategoryApiView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubCategoryApiView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class OrderApiView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class PaymentApiView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class RatingApiView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()


class ProductApiView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SeederUser(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        with open('/Users/macair/Documents/e-commerce/backend-drf/ecommerce/features/views/MOCK_DATA.json') as f:
            data_list = json.load(f)

        for data in data_list:
            otp_code = str(random.randint(100000, 1000000))

            user = User.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                otp_code=otp_code
            )
            # password = data.get('password')
            user.set_password(raw_password='holyboy191')
            user.save()
        return Response({'msg': "successful"})
