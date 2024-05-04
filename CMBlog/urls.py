from django.contrib import admin
from django.urls import path, include
from .views import index

# The line `import APIs` is importing a module named `APIs`. This module likely contains additional
# functionality related to APIs that will be used in the Django project. This could include API
# endpoints, serializers, or other API-related components.
from apis.blog_api import BlogList, BlogDetails, YourBlogs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('usersApp.urls')),
    path('blogs/', include('blogApp.urls')),
    path('', index, name="index"),
    
    # blog-apis
    path('api/blogs/', BlogList.as_view(), name='blog-list-api'),
    path('api/blog/create/', BlogList.as_view(), name='blog-create-api'),
    path('api/blog/detail/<int:blog_id>', BlogDetails.as_view(), name='blog-detail-api'),
    path('api/blog/edit/<int:blog_id>', BlogDetails.as_view(), name='blog-edit-api'),
    path('api/blog/delete/<int:blog_id>', BlogDetails.as_view(), name='blog-delete-api'),
    path('api/blog/yours', YourBlogs.as_view(), name='your-blogs-api'),
]
