python manage.py migrate
python manage.py create_admin
gunicorn api_core.wsgi:application -p 8000 & nginx -g "daemon off;"