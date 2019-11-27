from django.contrib import admin
from django.urls import path, include
from movies import views as movies_views

urlpatterns = [
    path('', movies_views.index),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
]
