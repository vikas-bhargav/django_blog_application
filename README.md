# Django Blog Application
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
   ![register](https://github.com/user-attachments/assets/15a4589a-2e86-46d4-84c7-bc6faa9c7718)

3. Login - http://localhost:8000/api/login/
   ![login](https://github.com/user-attachments/assets/06a3b52e-269e-4e50-911b-cb07ab026899)

5. Post List - http://localhost:8000/api/posts/
   ![post_list](https://github.com/user-attachments/assets/4812afb4-6a69-4f61-bd3a-37250eacc18d)
6. Post Create - http://localhost:8000/api/posts/
   ![create_post](https://github.com/user-attachments/assets/7522da17-38fe-4a23-a223-bf1462b70f2a)

10. Post Detail/Update/Delete - Post List - http://localhost:8000/api/posts/1
    ![update_delete_post](https://github.com/user-attachments/assets/0038d453-e420-4112-94eb-37b1cdd9c34f)
    
12. Comments List - http://localhost:8000/api/comments/
    ![comment_list](https://github.com/user-attachments/assets/9dd4bffc-7d60-4d3d-8eb6-ec568fe65ff1)

14. Comments Create - http://localhost:8000/api/comments/
    ![comment_added](https://github.com/user-attachments/assets/c804190d-3f73-4351-ad12-7877c05094cb)
15.
16. Comments Detail/Update/Delete - http://localhost:8000/api/comments/1/
      ![comment_added](https://github.com/user-attachments/assets/c0ebddb7-618b-4602-b203-350cb6fb4777)

17. Post Like/Unlike - http://localhost:8000/api/posts/1/like/
    ![post_liked](https://github.com/user-attachments/assets/a2263d25-1936-48d8-9f55-4fdda4fc8a68)
![post_unliked](https://github.com/user-attachments/assets/7cb8dcc3-b78c-4e0c-9dde-f932db797955)


