from django.urls import path
from . import views


urlpatterns = [
    path('password123001/',  views.index, name='mailapp-index'),
    path('',  views.mailform, name='mailapp-mailform'),
    path('success/', views.mailsuccess, name='mailapp-success'),

]

