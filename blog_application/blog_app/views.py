from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer


class PostListCreateAPIView(ListCreateAPIView):
    """Post create and list api view"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class PostRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    """Post update and delete api view"""
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CommentListCreateAPIView(ListCreateAPIView):
    """Post create and list api view"""
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CommentRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    """Post update and delete api view"""
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class UserRegistrationView(CreateAPIView):
    """User registration view"""
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(APIView):
    """User login view"""
    @staticmethod
    def post(request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)


class LikePost(APIView):
    """Like post view"""
    permission_classes = [permissions.IsAuthenticated]
    @staticmethod
    def post(request, pk):
        """Method for Post like or unlike by user"""
        post = get_object_or_404(Post, pk=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        else:
            post.likes.add(request.user)
            return Response({'status': 'liked'}, status=status.HTTP_200_OK)

