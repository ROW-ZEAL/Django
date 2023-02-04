from django.shortcuts import render


def login_details(request):
    context = {}
    return render(request, 'login/login.html', context)
