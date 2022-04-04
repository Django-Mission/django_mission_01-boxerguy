from unittest import result
from django.contrib import admin
from django.urls import path
from demos.views import lotto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
]
