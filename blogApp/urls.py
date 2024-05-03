from django.contrib import admin
from django.urls import path, include
from .views import blog_list_view, blog_detail_view, edit_blog, create_blog, your_blog, delete_blog

urlpatterns = [
    path('', blog_list_view, name='blog_list'),
    path('<int:blog_id>/', blog_detail_view, name='blog_details'),
    path('edit/<int:blog_id>', edit_blog, name = 'edit_blog'),
    path('create/', create_blog, name='create_blog'),
    path('yourblogs/', your_blog, name='your_blog'),
    path('delete/<int:blog_id>', delete_blog, name="delete_blog")
]
