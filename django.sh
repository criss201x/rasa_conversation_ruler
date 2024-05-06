#!/bin/bash
echo "Creando base de datos..."
python manage.py makemigrations rules
python manage.py makemigrations intension
python manage.py makemigrations mensaje_intension
python manage.py makemigrations respuesta
python manage.py makemigrations mensaje_respuesta
python manage.py makemigrations login
echo ====================================

echo "iniciando migraciones..."
python manage.py migrate
echo ====================================

echo ====================================
echo "creando admin..."
DJANGO_SUPERUSER_USERNAME='??' \
DJANGO_SUPERUSER_EMAIL='administrador_conversaciones@gmail.com' \
DJANGO_SUPERUSER_PASSWORD='??' \
python manage.py createsuperuser --noinput

python manage.py loaddata admin_interface_theme_bootstrap.json
python manage.py loaddata admin_interface_theme_foundation.json
python manage.py loaddata admin_interface_theme_uswds.json

echo "iniciando servidor..."
python manage.py runserver 0.0.0.0:8000
