from django.urls import path, include
from features.views import auth_views
from features.views import features_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', features_views.UserApiView)
router.register('brand', features_views.BrandApiView)
router.register('cart', features_views.CartApiView)
router.register('category', features_views.CategoryApiView)
router.register('subcategory', features_views.SubCategoryApiView)
router.register('order', features_views.OrderApiView)
router.register('payment', features_views.PaymentApiView)
router.register('rating', features_views.RatingApiView)
router.register('product', features_views.ProductApiView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register', auth_views.RegisterView.as_view(), name='register'),
    path('forgot_password', auth_views.ForgotPasswordView.as_view(),
         name='forgot_password'),
    path('verify', auth_views.VerifyView.as_view(), name='verify'),
    path('reset_password', auth_views.ResetPasswordView.as_view(),
         name='reset_password'),
    path('change_password', auth_views.ChangePasswordView.as_view(),
         name='change_password'),
    path('seeder_user', features_views.SeederUser.as_view(), name= 'seeder'),
]
