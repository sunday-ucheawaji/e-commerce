from django.contrib import admin
from features.models import Brand, Cart, Category, SubCategory, Order, Payment, Product, Rating
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Rating)


@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'is_verified', 'is_staff')
