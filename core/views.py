from django.shortcuts import render

# Create your views here.


def index(request):
    """View function returning the home page"""

    return render(request,'dashboard/dashboard.html')