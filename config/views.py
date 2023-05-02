from django.shortcuts import render
from django.http import HttpResponse




def home(request):

    context = {
        'lo':'asdasdadasd'
    }
    return render(request, 'accounts/home.html', context)