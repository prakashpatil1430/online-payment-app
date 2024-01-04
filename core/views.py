from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'user': request.user
    }
    return render(request, 'core/index.html', context)

# def shows(request):
#     return HttpResponse("hi")
