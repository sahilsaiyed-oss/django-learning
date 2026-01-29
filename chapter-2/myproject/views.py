from django.http import HttpResponse

def homepage(request):
    return HttpResponse("This is the Homepage")

def about(request):
    return HttpResponse("This is the About page")