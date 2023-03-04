from django.contrib import admin
from django.urls import path
from apps.core.views import frontpage, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('contact/', contact, name='contact'),
]
