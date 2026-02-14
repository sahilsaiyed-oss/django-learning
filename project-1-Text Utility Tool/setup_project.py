import os

# 1. Create Project and App folders
print("Creating project folders...")
os.system("django-admin startproject core .")
os.system("python manage.py startapp home")

# 2. Create the necessary directories
os.makedirs("home/templates/home", exist_ok=True)

# 3. Create home/urls.py
with open("home/urls.py", "w") as f:
    f.write("""from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze/', views.analyze, name='analyze'),
]""")

# 4. Write home/views.py
with open("home/views.py", "w") as f:
    f.write("""from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    uppercase = request.POST.get('uppercase', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    charcount = request.POST.get('charcount', 'off')

    purpose = ""
    params = {'original_text': djtext}

    if uppercase == "on":
        djtext = djtext.upper()
        purpose += "| Uppercase "

    if extraspace == "on":
        djtext = " ".join(djtext.split())
        purpose += "| Extra Spaces Removed "

    if charcount == "on":
        params['count'] = len(djtext)
        purpose += "| Character Counted "

    params['analyzed_text'] = djtext
    params['purpose'] = purpose
    return render(request, 'home/index.html', params)
""")

# 5. Write home/templates/home/index.html
with open("home/templates/home/index.html", "w") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Text Analyzer Pro</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>body { background-color: #f8f9fa; padding: 50px; } .card { padding: 20px; border-radius: 15px; shadow: 0 4px 15px rgba(0,0,0,0.1); }</style>
</head>
<body>
<div class="container">
    <div class="card">
        <h1 class="text-center mb-4">Text Analyzer Pro</h1>
        <form action="/analyze/" method="post">
            {% csrf_token %}
            <textarea class="form-control mb-3" name="text" rows="6">{{ original_text }}</textarea>
            <div class="d-flex justify-content-around mb-4">
                <label><input type="checkbox" name="uppercase"> Uppercase</label>
                <label><input type="checkbox" name="extraspace"> No Extra Space</label>
                <label><input type="checkbox" name="charcount"> Char Count</label>
            </div>
            <button type="submit" class="btn btn-primary w-100">Analyze</button>
        </form>
        {% if analyzed_text %}
        <hr><h3>{{ purpose }}</h3><div class="alert alert-success"><pre>{{ analyzed_text }}</pre></div>
        {% if count %}<p>Count: {{ count }}</p>{% endif %}{% endif %}
    </div>
</div>
</body>
</html>""")

# 6. Update core/urls.py
with open("core/urls.py", "w") as f:
    f.write("""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]""")

print("\nSuccess! Project structure created.")
print("IMPORTANT: Open 'core/settings.py' and add 'home' to INSTALLED_APPS manually.")