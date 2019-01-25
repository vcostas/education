from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('inbox', views.inbox, name='inbox'),
    path('compose', views.compose, name='compose'),
    path('sent', views.sent, name='sent'),
    path('drafts', views.drafts, name='drafts'),
    path('junk', views.junk, name='jumk'),
    path('trash', views.trash, name='trash'),

]