from django.shortcuts import render

from django.http import HttpResponse

def home(request):

   peoples = [
       {'name' : 'abhijeet Gupta' , 'age' : 18},
       {'name' : 'Rohan Sharma' , 'age' : 23},
       {'name' : 'Sahil saiyed' , 'age' : 21},
       {'name' : 'Sahil saiyed' , 'age' : 16},
        {'name' : 'Sahil saiyed' , 'age' : 17},
       
   ]

   for people in peoples:
       print(people)
       
   return render(request , "home/index.html" , context = {'peoples' : peoples})


def success_page(request):
    print("*" * 10)

    return HttpResponse("<h1> Hey this is a success page</h1>")