# django_blog_application
A simple blog application using Django and Django REST Framework, integrating basic CRUD (Create, Read, Update, Delete) functionalities.

# Steps to setup and start project

1. Create new dir ->>  mkdir <project_name>
2. Create virtual env ->>  Python3 -m venv env
3. Activate virtual environment >> source env/bin/activate
4. Clone repo from git >> git clone git@github.com:vikas-bhargav/django_blog_application.git
5. Go to folder >> cd /blog_application
6. Install requirements >>  install -r /path/to/requirements.txt
7. Setup database >> python manage.py migrate
8. Run server >>  python manage.py runserver
9. Test apis on browser >> http://127.0.0.1:8000/api/




# Blog APIs

1. Register user - http://localhost:8000/api/register/
2. Login - http://localhost:8000/api/login/
3. Post List - http://localhost:8000/api/posts/
4. Post Detail - Post List - http://localhost:8000/api/posts/1
5. Post Detail/Update/Delete - Post List - http://localhost:8000/api/posts/1
6. Comments List - http://localhost:8000/api/comments/
7. Comments Detail/Update/Delete - http://localhost:8000/api/comments/1/
8. Post Like/Unlike - http://localhost:8000/api/posts/1/like/
    