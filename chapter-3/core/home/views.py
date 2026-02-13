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


   text = """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima reprehenderit accusantium excepturi commodi amet modi nulla, architecto dolor libero cupiditate. Dignissimos fugiat possimus asperiores nam, assumenda quibusdam! Praesentium, sit assumenda.
"""
   for people in peoples:
       print(people)
       
   return render(request, "home/index.html", {
    'peoples': peoples,
    'text': "text"
})

def about(request):
    return render(request,"home/about.html")


def contact(request):
    return render(request,"home/contact.html")


def success_page(request):
    print("*" * 10)

    return HttpResponse("<h1> Hey this is a success page</h1>")