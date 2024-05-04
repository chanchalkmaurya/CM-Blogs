from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from blogApp.models import Blog
from blogApp.forms import BlogCreationForm
from apis.blog_api import BlogList, BlogDetails, YourBlogs


# Regular Django views for rendering HTML templates
def blog_list_view(request):
    api_view = BlogList.as_view()
    response = api_view(request)
    
    if response.status_code == 200:
        blogs = response.data
        return render(request, 'blogpages/bloglist.html', {'blogs': blogs})
    else:
        # Handle error response
        return render(request, 'blogpages/error.html', {'error_message': 'Failed to fetch blog list'})

def blog_detail_view(request, blog_id):
    api_view = BlogDetails.as_view()
    response = api_view(request, blog_id=blog_id)
    if response.status_code == 200:
        blog = response.data
        author = User.objects.get(pk=response.data['author'])
        # check if logged in user is the author of the opened blog
        is_author = False
        if request.user == author:
            is_author = True
            
        return render(request, 'blogpages/blogdetail.html', {
            'blog': blog,
            'author':author,
            'is_author': is_author
            
            })
    else:
        # Handle error response
        return render(request, 'blogpages/error.html', {'error_message': 'Failed to fetch blog details'})
    
    
    
def edit_blog(request, blog_id):
    api_view = BlogDetails.as_view()
    response = api_view(request, blog_id=blog_id)
    
    context = {
        'title': 'Edit Blog',
        'blog' : response.data,
        'status_code': response.status_code
    }
        
    if request.method == "POST":
        status_code = response.status_code
        if status_code == 200:
            messages.success(request, ("Updated Successfully"))
            return redirect('your_blog')
        
        elif status_code == 400:
            return render(request, 'blogpages/error.html', {'error_message': 'Failed to update.'})
        
        elif status_code == 403:
            return render(request, 'blogpages/error.html', {'error_message': 'Access Denied'})
            
    return render(request, 'blogpages/editblog.html', context)
    


@login_required
def create_blog(request):
    api_view = BlogList.as_view()
    response = api_view(request)
    
    if response.status_code == 201:
        messages.success(request, ("Blog Created Successfully"))
        return redirect('blog_list')
    
    form = BlogCreationForm()
    context = {
        'form': form,
        # 'status_code':response.status_code,
    }
    return render(request, 'blogpages/createblog.html', context)



def your_blog(request):
    api_view = YourBlogs.as_view()
    response = api_view(request)
    if response.status_code == 200:
        blogs = response.data
        return render(request, 'blogpages/yourblogs.html', {'blogs': blogs})
    else:
        # Handle error response
        return render(request, 'blogpages/error.html', {'error_message': 'Failed to fetch blog list'})
    
    
def delete_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    
    if request.user == blog.author:
        blog.delete()
        messages.success(request, "Blog Deleted Successfully")
        return redirect('your_blog')
    
    else:
        return render(request, 'blogpages/error.html', {'error_message': 'Access Denied'})
