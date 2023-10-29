from django.contrib import admin
from django.urls import path
from mainApp.views import result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', result)
]
