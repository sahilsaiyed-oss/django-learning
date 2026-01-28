from django.shortcuts import render

def home(request):
    # This tells Django to look in your 'templates' folder for home.html
    return render(request, 'home.html')

def about(request):
    # This tells Django to look for about.html
    return render(request, 'about.html')