from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)

urlpatterns = [
   
    
    path('login/', views.userLogin, name='user_login'),
    path('factorLogin/', views.factorLogin, name='user_factorLogin'),
    path('logout/', views.userLogout, name='user_logout'),
    path('createUser/', views.createUser, name='create_User'),
    path('inlogin/', views.inlogin, name='in_login'),
    path('logincreateUser/', views.logincreateUser, name='login_create_User'),
    path('userPasswordReset/', views.userPasswordReset, name='user_passwordReset'),
    path('passwordChange/', views.passwordChange, name='passwordChange'),
    path('forgotPasswordAcces/', views.forgotPasswordAcces, name='Forgot_Password_Acces'),
    path('accountType/', views.accountType, name='account_Type'),
    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),
    path('sekreterDashboard/', views.sekreterDashboard, name='sekreterDashboard'),
    path('api/token/access/', TokenRefreshView.as_view(), name='token_get_access'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   

]


#  path('', views.myAccount),
#     
#    