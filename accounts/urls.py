from django.urls import path, include
from . import views


urlpatterns = [
   
    
    path('login/', views.userLogin, name='user_login'),
    path('factorLogin/', views.factorLogin, name='user_factorLogin'),
    path('logout/', views.userLogout, name='user_logout'),
    path('createUser/', views.createUser, name='create_User'),
    path('userPasswordReset/', views.userPasswordReset, name='user_passwordReset'),
    path('passwordChange/', views.passwordChange, name='passwordChange'),
    path('forgotPasswordAcces/', views.forgotPasswordAcces, name='Forgot_Password_Acces'),
    
   

]


#  path('', views.myAccount),
#     
#    