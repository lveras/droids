#!/bin/bash

python manage.py makemigrations
python manage.py migrate --run-syncdb

echo "from django.contrib.auth import get_user_model;
User = get_user_model();
User.objects.create_user('luke', 'luke@droids.com', 'luke')
User.objects.create_superuser('admin', 'admin@droids.com', 'admin')" |
python manage.py shell

python manage.py runserver 0.0.0.0:8000