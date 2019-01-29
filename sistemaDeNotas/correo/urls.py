from . import views
from django.urls import path, include

app_name='correo'
urlpatterns = [
    path('', views.index, name='index'),
    path('inbox/', views.inbox, name='inbox'),
    path('compose/', views.compose, name='compose'),
    path('sent/', views.sent, name='sent'),
    path('drafts/', views.drafts, name='drafts'),
    path('junk/', views.junk, name='junk'),
    path('trash/', views.trash, name='trash'),

]