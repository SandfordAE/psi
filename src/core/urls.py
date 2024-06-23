from django.contrib import admin
from django.urls import path

from .views import home_page_view

urlpatterns = [
    path("", home_page_view),
    path("Hello-World", home_page_view),
    path("admin/", admin.site.urls),
]

