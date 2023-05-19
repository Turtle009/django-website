from django.contrib import admin
from django.urls import path, include
from homepage.views import homepage
from aboutme.views import aboutme

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('aboutme/', aboutme),
    path('', homepage),
]
