from django.shortcuts import render

# Create your views here.


def hr_view(request):

    return render(request,'hr.html')