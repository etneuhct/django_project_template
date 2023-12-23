python manage.py collectstatic
python docker/generate_nginx_conf.py
cp nginx_config.conf /etc/nginx/conf.d/django_app.conf
python manage.py migrate
python manage.py create_admin
gunicorn api_core.wsgi:application -p 8000 & nginx -g "daemon off;"