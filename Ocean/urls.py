from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('battle.urls')),
    path('about/', include('about.urls')),
    path('login/', include('login.urls')),
    path('career/', include('career.urls')),

]
