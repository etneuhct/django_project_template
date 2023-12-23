python docker/generate_nginx_conf.py
copy nginx_config.conf /etc/nginx/conf.d/django_app.conf
python manage.py migrate
python manage.py create_admin
uvicorn api_core.asgi:application --port 8000 & nginx -g "daemon off;"
