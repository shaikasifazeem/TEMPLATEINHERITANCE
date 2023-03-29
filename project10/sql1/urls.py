from sql1.views import *
from django.urls import path
app_name='rolex'
urlpatterns=[
    path('rolex/',rolex,name='rolex'),
]