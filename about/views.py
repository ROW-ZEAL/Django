from django.shortcuts import render


def show_about(request):
    context = {}
    return render(request, 'about/root.html', context)
