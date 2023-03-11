https://github.com/llorenss/dj_very_academy2

Django Rest Framework Series - Build a Django DRF app and React Front-end - Part-1
https://youtu.be/soxd_xdHR0o

windows vs code
py -m venv ve
ve\Scripts\Activate.ps1

В кавычках команду ниже
'C:\Python\dj_very_academy1\ve\Scripts\python.exe -m pip install --upgrade pip'
Или попробовать с кавычками и без
'python -m pip install --upgrade pip'

pip install django

django-admin startproject core .

py manage.py startapp blog

py manage.py startapp blog_api

pip install black

black "--line-length=79" core/
black "--line-length=79" blog/
black "--line-length=79" blog_api/

windows
python manage.py runserver

http://127.0.0.1:8000/

Создадим локальный репозиторий в папке с проектом:
git init

git status

https://youtu.be/soxd_xdHR0o?t=2860

python manage.py makemigrations
python manage.py migrate

python manage.py makemigrations --dry-run --verbosity 3

pip install djangorestframework

https://youtu.be/soxd_xdHR0o?t=3691
заполнить сериалайзер и вью в блогапи.

http://127.0.0.1:8000/api/

python manage.py createsuperuser

https://youtu.be/soxd_xdHR0o?t=4421

pip install coverage

Исключаем при тестировании папку:
coverage run --omit='_/ve/_' manage.py test

coverage html

Скопировать путь для браузера
file:///C:/Python/dj_very_academy2/htmlcov/index.html

https://youtu.be/soxd_xdHR0o?t=5515

https://youtu.be/soxd_xdHR0o?t=6815
pip install django-cors-headers
https://pypi.org/project/django-cors-headers/

permission levels
https://youtu.be/5AOn0BmSXyE?t=162

<!-- https://www.django-rest-framework.org/api-guide/permissions/#isauthenticated -->

We can apply permissions: - project-level - view-level - object-level

Permissions -> HTTP Requests

- Permissions:
  - View -> GET
  - Delete -> DELETE
  - Change -> PUT PATCH
  - Add -> POST

Custom permissions
https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions

https://youtu.be/5AOn0BmSXyE?t=1877

🐱‍🏍Testing the custom permission

https://youtu.be/AfYfvjP1hK8?t=1184

jwt token

pip install djangorestframework-sipmlejwt

https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html


https://github.com/veryacademy/YT-Django-DRF-Simple-Blog-Series-JWT-Part-3

py manage.py startapp users