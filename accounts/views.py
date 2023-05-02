from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User, UserProfile
from .forms import UserForm
from django.contrib import messages, auth


def createUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('create_User')
    elif request.method == 'POST':
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
    return render(request, 'accounts/createUser.html', context)
    
   
    # context = {
    #     'lo':'loginden geldin',
    # }
    # return render(request, 'accounts/createUser.html', context)






def userLogin(request):

    context = {
        'lo':'loginden geldin',
    }
    return render(request, 'accounts/userLogin.html', context)




def factorLogin(request):

    context = {
        'lo':'loginden geldin',
    }
    return render(request, 'accounts/factorLogin.html', context)


def userLogout(request):

    context = {
        'lo':'loginden geldin',
    }
    return render(request, 'accounts/logout.html', context)



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



def passwordChange(request):

    context = {
        'lo':'loginden geldin',
    }
    return render(request, 'accounts/passwordChange.html', context)


# Set Password