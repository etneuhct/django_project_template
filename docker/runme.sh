python manage.py migrate
python manage.py create_admin
gunicorn {{project_name}}.wsgi:application -p 8000 & nginx -g "daemon off;"