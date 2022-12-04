python manage.py migrate
python manage.py create_admin
sh run_celery.bat & sh run_celery_beat.bat & gunicorn {{project_name}}.wsgi:application -p 8000 & nginx -g "daemon off;"