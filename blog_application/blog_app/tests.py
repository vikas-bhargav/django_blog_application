import pytest
from django.contrib.auth.models import User
from .models import Post, Comment


def get_or_create_user() -> User:
    """Create user and return user instance."""
    user = User.objects.create_user(username='tester', password='test@123')
    return user


@pytest.mark.django_db
def test_post_creation():
    """Test creating a new post."""
    user = get_or_create_user()
    post = Post.objects.create(
        title="Test Post",
        content="Test Content",
        author=user
    )
    assert post.title == "Test Post"
    assert post.content == "Test Content"
    assert post.author.id == user.id


@pytest.mark.django_db
def test_post_str():
    """Test string representation of post."""
    user = get_or_create_user()
    post = Post.objects.create(
        title="Test Post",
        content="Test Content",
        author=user
    )
    assert str(post) == "Test Post"


@pytest.mark.django_db
def test_comment_creation():
    """Test creating a new comment."""
    user = get_or_create_user()
    post = Post.objects.create(
        title="Test Post",
        content="Test Content",
        author=user
    )
    comment = Comment.objects.create(
        post=post,
        author=user,
        text="Comment Text"
    )
    assert comment.post == post
    assert comment.author == user
    assert comment.text == "Comment Text"


@pytest.mark.django_db
def test_comment_str():
    """Test string representation of comment."""
    user = get_or_create_user()
    post = Post.objects.create(
        title="Test Post",
        content="Test Content",
        author=user
    )
    comment = Comment.objects.create(
        post=post,
        author=user,
        text="Comment Text"
    )
    assert str(comment) == "Comment Text"