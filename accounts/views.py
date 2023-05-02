from django.shortcuts import render
from django.http import HttpResponse



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


def createUser(request):

    context = {
        'lo':'loginden geldin',
    }
    return render(request, 'accounts/createUser.html', context)



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