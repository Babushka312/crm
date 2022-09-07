from django.shortcuts import render
from rest_framework import permissions, status
from .serializers import PostSerializer
from account.permissions import IsOwnerOrReadOnly
from blog.models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


class PostListApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostUpdateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404

    def put(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDeleteApiView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




