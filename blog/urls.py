from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('add/', views.post_edit, name='post_add'),
    path('mod/<int:post_id>/', views.post_edit, name='post_mod'),
    path('del/<int:post_id>/', views.post_del, name='post_del')
]