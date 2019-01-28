from django.shortcuts import render

# Create your views here.


def lunch(request):

    return render(request, 'lunch.html')
