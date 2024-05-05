from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from blogApp.models import Blog
from blogApp.forms import BlogCreationForm
from apis.blog_api import BlogList, BlogDetails, YourBlogs

from django.core.paginator import Paginator

# views
def blog_list_view(request):
    api_view = BlogList.as_view()
    response = api_view(request)

    if response.status_code == 200:
        # Either get or post request successfully executed
        blogs = response.data
        
        # adding pagination concept to this view
        paginator = Paginator(blogs, 5)  # Show 5 blogs per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # context data to be passed in template => 'blogpages/bloglist.html'
        context = {
            'blogs': page_obj,
            'title': 'All blogs',
            'paginator': paginator,
        }

        return render(request, 'blogpages/bloglist.html', context)
    else:
        # Handle error response
        
        # context data to be passed in template => 'blogpages/error.html'
        context = {
            'error_message': 'Failed to fetch blog list',
            'title': 'Error Page'
        }
        return render(request, 'blogpages/error.html', context)


def blog_detail_view(request, blog_id):
    api_view = BlogDetails.as_view()
    response = api_view(request, blog_id=blog_id)
    
    if response.status_code == 200:
        # get the response data of BlogDetails.as_view(), passed with param : blog_id
        # it can be get or post request's response
        blog = response.data
        
        # get the author of current blog
        author = User.objects.get(pk=response.data['author'])
        
        # check if logged in user is the author of the current blog 
        is_author = False
        if request.user == author:
            is_author = True
        
        # context to be passed with the template => 'blogpages/blogdetail.html'
        context = {
            'blog': blog,
            'author':author,
            'is_author': is_author,
            'title': 'Blog Detail Page'
        }
        return render(request, 'blogpages/blogdetail.html',context)
    else:
        # Handle error response
        # context data to be passed in template => 'blogpages/error.html'
        context = {
            'error_message': 'Failed to fetch blog details',
            'title':'Error Page'
            }
        return render(request, 'blogpages/error.html', context)
    
    
def edit_blog(request, blog_id):
    api_view = BlogDetails.as_view()
    response = api_view(request, blog_id=blog_id)
    
    if request.method == "POST":
        status_code = response.status_code
        if status_code == 200:
            messages.success(request, ("Updated Successfully"))
            return redirect('your_blog')
        
        elif status_code == 400:
            # context data to be passed in template => 'blogpages/error.html'
            context = {
                'error_message': 'Failed to update.',
                'title':'Error Page'
            }
            return render(request, 'blogpages/error.html', context)
        
        elif status_code == 403:
            # context data to be passed in template => 'blogpages/error.html'
            context = {
                'error_message': 'Access Denied',
                'title':'Error Page'
            }
            return render(request, 'blogpages/error.html', context)
    
    # context data to be passed in template => 'blogpages/editblog.html'
    context = {
        'title': 'Edit Blog',
        'blog' : response.data,
    }
    return render(request, 'blogpages/editblog.html', context)
    


@login_required
def create_blog(request):
    api_view = BlogList.as_view()
    response = api_view(request)
    
    # check the response_status_code
    if response.status_code == 201:
        messages.success(request, ("Blog Created Successfully"))
        return redirect('blog_list')
    
    # include BlogCreationForm
    form = BlogCreationForm()
    
    context = {
        'title':'Create Blog',
        'form': form        
    }
    return render(request, 'blogpages/createblog.html', context)



def your_blog(request):
    api_view = YourBlogs.as_view()
    response = api_view(request)
    
    # check the response status code
    if response.status_code == 200:
        blogs = response.data
        
        # implement pagination concept
        paginator = Paginator(blogs, 5)  # Show 5 blogs per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # context to be passed with the template => 'blogpages/yourblog.html'
        context = {
            'blogs': page_obj,
            'title':'Your Blogs',
            'paginator': paginator
        }
        return render(request, 'blogpages/yourblogs.html', context)
    else:
        # Handle error response
        # context to be passed with the template => 'blogpages/error.html'
        context = {
            'error_message': 'Failed to fetch blog list',
            'title':'Error Page'
        }
        return render(request, 'blogpages/error.html', context)
    
    
def delete_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    # check if the current user is the author of blog
    if request.user == blog.author:
        blog.delete()
        messages.success(request, "Blog Deleted Successfully")
        return redirect('your_blog')
    
    else:
        # handle the error message
        context = {
            'error_message': 'Access Denied',
            'title':'Error Page'
        }
        return render(request, 'blogpages/error.html', context)
