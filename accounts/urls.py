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
#     path('myAccount/', views.myAccount, name='myAccount'),
#     path('forgot_password/', views.forgot_password, name='forgot_password'),
#     path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
#     path('reset_password/', views.reset_password, name='reset_password'),
