from django.urls import path, re_path
from qa.views import test

urlpatterns = [
    re_path(r'', test),   
]