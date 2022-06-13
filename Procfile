release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn mozio.wsgi:application -b 0.0.0.0:$PORT