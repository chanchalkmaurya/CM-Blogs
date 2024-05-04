from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from blogApp.models import Blog
from blogApp.serializers import BlogSerializer


class BlogList(APIView):
    def get(self, request):
        # logging.info("Blog List Get method")
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # Create a mutable copy of the request data
        mutable_data = request.data.copy()
        
        # Add the 'author' field to the mutable data dictionary
        mutable_data['author'] = request.user.id
        
        # Create a serializer instance with the modified data
        serializer = BlogSerializer(data=mutable_data)
        
        # Check if the data passes validation
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class YourBlogs(APIView):
    def get(self, request):
        blogs = Blog.objects.filter(author=request.user.id)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class BlogDetails(APIView):
    def get_object(self, blog_id):
        try:
            return Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            raise Http404
        
        
    def get(self, request, blog_id):
        print("GET method called for blog ID:", blog_id)
        blog = self.get_object(blog_id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, blog_id):
        blog = self.get_object(blog_id)
        mutable_data = request.data.copy()
        # Add the 'author' field to the mutable data dictionary
        mutable_data['author'] = request.user.id
        # Create a serializer instance with the modified data
        serializer = BlogSerializer(blog, data=mutable_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response(status=status.HTTP_403_FORBIDDEN)