https://github.com/llorenss/dj_very_academy2

Django Rest Framework Series - Build a Django DRF app and React Front-end - Part-1
https://youtu.be/soxd_xdHR0o

windows vs code
    py -m venv ve
    ve\Scripts\Activate.ps1

В кавычках команду ниже
'C:\Python\dj_very_academy1\ve\Scripts\python.exe -m pip install --upgrade pip'

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


Started lesson:
https://www.youtube.com/@veryacademy
Django DRF Project | Modularizing Django Settings | 2
https://youtu.be/0WXVAMGisWs

python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
m0zl&+r%jyb0$6l+7@v)qaclmgq2awf^4_cj1b5=qm&uwvk5$c

    Use quit() or Ctrl-Z plus Return to exit

pip freeze > requirements.txt

pip install -r requirements.txt

https://pypi.org/project/python-dotenv/

pip install python-dotenv

pip install djangorestframework

https://pypi.org/

https://www.django-rest-framework.org/

https://pypi.org/project/pytest/

pip install pytest==7.2.2

(ve) (base) PS C:\Python\dj_very_academy> pytest

pytest -h

pip instal pytest-django==4.5.2

https://pytest-django.readthedocs.io/en/latest/

# -- FILE: pytest.ini (or tox.ini)

[pytest]
DJANGO_SETTINGS_MODULE = test.settings

# -- recommended but optional:

python*files = tests.py test*_.py _\_tests.py

.vscode
settings.json
{
"editor.formatOnSave": true,
"editor.fontWeight": "normal",
"editor.fontFamily": "Fira Code",
"editor.minimap.enabled": false,
"python.formatting.provider": "black",
"python.formatting.blackArgs": [
"--line-length",
"79"
],
"[python]": {
"editor.codeActionsOnSave": {
"source.organizeImports": true
},
"editor.formatOnType": true,
},
"files.autoSave": "afterDelay",
"workbench.iconTheme": "material-icon-theme",
}

pip install flake8

python manage.py startapp product ./drfecommerce/product

pip install django-mptt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

https://pypi.org/search/?q=drf-spectacular&o=

pip install drf-spectacular

INSTALLED_APPS = [
...
"drf_spectacular",
...
]

REST_FRAMEWORK = {
"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPRECTACULAR_SETTINGS = {
"TITLE": "Django DRF Ecommerce",
}

python manage.py spectacular --file shcema.yml

http://127.0.0.1:8000/api/schema/docs
http://127.0.0.1:8000/api/schema/docs#/api/api_brand_list
http://127.0.0.1:8000/api/brand/


 Django DRF Project | Implimenting Product | 20 

 http://127.0.0.1:8000/api/schema/docs#/api/api_product_list


 pip install coverage

 coverage run -m pytest

 coverage html

 pip install pytest-cov

 pytest --cov

 Unit Test

class TestCategoryModel

pip install pytest-factoryboy