from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('generate-email/', GenerateMailView.as_view(), name='generate-email'),
    path('get-inbox/<str:email>', GetInboxView.as_view(), name='get-inbox'),
]
