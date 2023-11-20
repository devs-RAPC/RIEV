from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RIEVS.urls')),
    path('users/', include('users.urls')),
]
