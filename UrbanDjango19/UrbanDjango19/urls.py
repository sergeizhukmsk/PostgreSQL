from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task1/', include('task1.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]