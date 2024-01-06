from django.shortcuts import render


def index(request):
    user = ''
    if request.user.is_authenticated:
        user = request.user
    context = {
        'user': user
    }
    return render(request, 'core/index.html', context)
