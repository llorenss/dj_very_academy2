from rest_framework import generics
from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
    DjangoModelPermissions,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,

)

from blog.models import Post

from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PostUserWritePermission(BasePermission):
    message = "Editing posts is resrticted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    # define custom queryset
    def get_queryset(self):
        return Post.objects.all()


# from django.shortcuts import get_object_or_404

# def my_view(request):
#     obj = get_object_or_404(MyModel, pk=1)

# Этот пример эквивалентен:

# from django.http import Http404

# def my_view(request):
#     try:
#         obj = MyModel.objects.get(pk=1)
#     except MyModel.DoesNotExist:
#         raise Http404("No MyModel matches the given query.")


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()

#     def list(self,request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
    
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)
    
# class UserViewSet(viewsets.ViewSet):
#     """
#     Example empty viewset demonstrating the standard
#     actions that will be handled by a router class.

#     If you're using format suffixes, make sure to also include
#     the `format=None` keyword argument for each action.
#     """

#     def list(self, request):
#         pass

#     def create(self, request):
#         pass

#     def retrieve(self, request, pk=None):
#         pass

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
        # pass

# class PostList(generics.ListCreateAPIView):
#     permission_classes = [
#         IsAuthenticatedOrReadOnly,
#     ]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer


# class PostDetail(
#     generics.RetrieveUpdateDestroyAPIView,
#     PostUserWritePermission,
# ):
#     permission_classes = [
#         PostUserWritePermission,
#     ]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
