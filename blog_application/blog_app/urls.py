from django.urls import path
from . import views

urlpatterns = [
    # List and Create view
    path('posts/', views.PostListCreateAPIView.as_view(), name='post-list-create'),
    path('comments/', views.CommentListCreateAPIView.as_view(), name='comment-list-create'),
    # Retrieve, Update, and Delete view
    path('posts/<int:pk>/', views.PostRetrieveUpdateDeleteAPIView.as_view(), name='post-retrieve-update-destroy'),
    path('posts/<int:pk>/like/', views.LikePost.as_view(), name='like-post'),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDeleteAPIView.as_view(), name='comment-retrieve-update-destroy'),
    # User login
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
]