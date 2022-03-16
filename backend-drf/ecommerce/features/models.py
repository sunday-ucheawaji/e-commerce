from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
import random


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        otp_code = str(random.randint(100000, 1000000))

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_verified', True)
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')

        if extra_fields.get('is_verified') is not True:
            raise ValueError('Superuser must have is_verified=True.')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields, otp_code=otp_code)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    otp_code = models.CharField(
        default=None, max_length=6)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']
    objects = CustomUserManager()

    def __str__(self):
        return self.email + " " + str(self.id)


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Brands'


class Cart(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, )
    products = models.JSONField(encoder=None)
    total_cost = models.DecimalField(max_digits=9, decimal_places=2)
    coupon = models.BooleanField(default=False)

    def __str__(self):
        return self.products


class Category(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    PROCESSING_STOCK = 'Processing Stock'
    DELIVERY_IN_PROGRESS = 'Delivery in Progress'
    DELIVERED = 'Delivered'
    NOT_DELIVERED = 'Not Delivered'
    RETURNED = 'Returned'
    DELIVERY_STATUSES = [
        (PROCESSING_STOCK, 'Processing Stock'),
        (DELIVERY_IN_PROGRESS, 'Delivery in Progress'),
        (DELIVERED, 'Delivered'),
        (NOT_DELIVERED, 'Not Delivered'),
        (RETURNED, 'Returned'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_id = models.ForeignKey(
        Cart, on_delete=models.PROTECT)
    delivery_address = models.TextField()
    delivery_status = models.CharField(
        max_length=20, choices=DELIVERY_STATUSES, null=True)

    def __str__(self):
        return self.delivery_status


class Payment(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(
        Order,  on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    otp_code = models.CharField(max_length=6, unique=True, null=True)
    email_verified = models.BooleanField(default=False)
    status = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.status


class Product(models.Model):

    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'

    SIZE_CHOICES = [
        (LARGE, 'Large'),
        (MEDIUM, 'Medium'),
        (SMALL, 'Small'),
    ]

    WHITE = 'WH'
    BLUE = 'BL'
    RED = 'RE'
    BLACK = 'BK'
    BROWN = 'BR'

    COLOUR_CHOICES = [
        (WHITE, 'White'),
        (BLUE, 'Blue'),
        (RED, 'Red'),
        (BLACK, 'BK'),
        (BROWN, 'Brown'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    image = models.URLField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField()
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(
        max_length=50, choices=SIZE_CHOICES, default=MEDIUM)
    description = models.TextField(max_length=50)
    colour = models.CharField(
        max_length=50, choices=COLOUR_CHOICES, default=BLACK)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-created_at']


class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score = models.FloatField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    review = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.review


class SubCategory(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
