from django.shortcuts import render


def career(request):
    context = {}
    return render(request, 'career/root.html', context)
