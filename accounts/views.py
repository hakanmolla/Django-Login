from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User, UserProfile
from .forms import UserForm
from django.contrib import messages, auth
from .utils import detectUser
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied



# Restrict the vendor from accessing the customer page
def check_role_user(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied


def logincreateUser(request):
    messages.warning(request, 'You are already logged in! Login durumdasınız')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Create the user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()
            # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = form.cleaned_data['role']
            user.save()

            # Send verification email
            # mail_subject = 'Please activate your account'
            # email_template = 'accounts/emails/account_verification_email.html'
            # send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'Your account has been registered sucessfully!')
            return redirect('create_User')
        else:
            print('invalid form')
            messages.error(request,form.errors,)
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/logincreateUser.html', context)

def createUser(request):
    
    if request.user.is_authenticated:
        # messages.warning(request, 'You are already logged in! ')
        return redirect('login_create_User')
    elif request.method == 'POST':
        print()
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            # Create the user using the form
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()
            # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = form.cleaned_data['role']
            user.save()

            # Send verification email
            # mail_subject = 'Please activate your account'
            # email_template = 'accounts/emails/account_verification_email.html'
            # send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'Your account has been registered sucessfully!')
            return redirect('create_User')
        else:
            print('invalid form')
            messages.error(request,form.errors,)
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/createUser.html', context)
    
   
    # context = {
    #     'lo':'loginden geldin',
    # }
    # return render(request, 'accounts/createUser.html', context)

def inlogin(request):

    return render(request, 'accounts/inlogin.html', )

def userLogin(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return render(request, 'accounts/inlogin.html', )
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('in_login')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('in_login')
    return render(request, 'accounts/userLogin.html')
 
def userLogout(request):
    
    auth.logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('user_login')

def passwordChange(request):

    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            pk = request.user.id
            print(pk)
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('user_login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('passwordChange')
    return render(request, 'accounts/passwordChange.html')   


def accountType(request):
    user = request.user
    redirectUrl = detectUser(user)
    
    return redirect(redirectUrl)



def factorLogin(request):

    context = {
        'lo':'loginden geldin',
    }
    return render(request, 'accounts/factorLogin.html', context)

def userPasswordReset(request):

    context = {
        'lo':'loginden geldin',
    }
    return render(request, 'accounts/userPasswordReset.html', context)

def forgotPasswordAcces(request):

    context = {
        'lo':'loginden geldin',
    }
    return render(request, 'accounts/forgotPasswordAcces.html', context)

#Pages 

def adminDashboard(request):
    
    context = {
            'lo':'loginden geldin',
        }
    return render(request, 'accounts/adminDashboard.html', context)


@login_required(login_url='user_login')
@user_passes_test(check_role_user)
def sekreterDashboard(request):
    
    context = {
            'lo':'loginden geldin',
        }
    return render(request, 'accounts/sekreterDashboard.html', context)