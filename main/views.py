from django.shortcuts import render, redirect
from .models import Survey



def index(request):
    return render(request, 'main/index.html', {})

def survey(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login?next=/survey") 

    elif request.method == "GET":
        return render(request, 'main/survey.html', {})

    elif request.method == "POST":
        survey = Survey()
        survey.name = request.POST.get("name", "")
        survey.address = request.POST.get("address", "")
        survey.email = request.POST.get("email", "")
        survey.phone_number = request.POST.get("phone_number", "")
        survey.save()
        return render(request, 'main/survey.html', {})
