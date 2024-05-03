from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('usersApp.urls')),
    path('blogs/', include('blogApp.urls')),
    path('', index, name="index")
]
