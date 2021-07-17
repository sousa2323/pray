from django.urls import path

from .views import PageView

app_name = 'core'

urlpatterns = [
    path('', PageView.as_view(), name='page-view'),
    
]
