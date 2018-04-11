# Simple Site builded on django-rest-framework

You can create a simple web application using django-rest-framework. 


# How to install on ubuntu linux

At first you need to download and install python3 if you already haven't: http://python.org .
```buildoutcfg
apt install python3
apt install pip3
```

Install virtualenv:
```buildoutcfg
pip3 install virtualenv 
```
Install git:
```buildoutcfg
apt install git
```

Clone this repo:
```buildoutcfg
cd ~/your_projects_dir
git clone https://github.com/kheeva/otus_fs_dz7_django_rest_framework
```

Make a virtual env:
```bash
cd otus_fs_dz7_django_rest_framework
virtualenv venv
source venv/bin/activate
```

Install all the modules:
```
pip install -r requirements.txt
```

Create .env file in the root of your_project_dir.
Customize your settings inside .env:
```
DJANGO_SECRET_KEY=your_secret_key
```
Also you can move database settings from settings.py to the .env file.

After that your django software should work.
```buildoutcfg
./manage.py migrate
./manage.py createsuperuser
```

# How to use
Read the documentation and customize settings.

# Testing

```
python manage.py runserver 0.0.0.0:8000
```

Getting list of courses:

```http://127.0.0.1:8000/api/courses/```

Filtering some fields:

`http://127.0.0.1:8000/api/courses/?fields=title,price`

`http://127.0.0.1:8000/api/courses/?fields!=id`

Filter by content inside fields:

`http://127.0.0.1:8000/api/courses/?search=Python`

Different filters in one request:

`http://127.0.0.1:8000/api/courses/?fields=title,price&search=Python&price=9500`


# Project Goals

The code is written for educational purposes. Training courses: otus.ru)
