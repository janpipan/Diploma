python3 manage.py migrate
gunicorn --bind :8000 --workers 3 djangodatabase.wsgi