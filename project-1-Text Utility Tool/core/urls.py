from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler404

# Point to your custom view
handler404 = 'home.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]