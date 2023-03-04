from django.contrib import admin
from django.urls import path
from apps.core.views import frontpage, contact
from apps.store.views import product_detail, category_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),
    path('contact/', contact, name='contact'),
]
