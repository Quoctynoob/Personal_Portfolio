from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myportfolio/index.html')

def about(request):
    return render(request, 'myportfolio/about.html')

def projects(request):
    return render(request, 'myportfolio/projects.html') 

def contact(request):
    return render(request, 'myportfolio/contact.html')




