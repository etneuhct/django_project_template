import os

import urllib.parse


def extract_server_name(url):
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.netloc


nginx_template = """
server {{
    listen 80;
    server_name {api_server_name};

    location /api {{
        proxy_pass http://localhost:8000;
        include proxy_params;
    }}
}}

server {{
    listen 80;
    server_name {admin_server_name};

    location /admin {{
        proxy_pass http://localhost:8000;
        include proxy_params;
    }}
}}

server {{
    listen 80;
    server_name {ws_server_name};

    location /ws {{
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }}
}}

server {{
    listen 80;
    server_name {statics_server_name};

    location /statics {{
        alias /usr/src/app/statics;
        proxy_set_header X-Forwarded-Proto https;
    }}
}}

server {{
    listen 80;
    server_name {medias_server_name};

    location /medias {{
        alias /usr/src/app/medias;
        proxy_set_header X-Forwarded-Proto https;
    }}
}}
"""

api_server_url = os.getenv("API_SERVER_URL", "http://api.localhost/api/")
admin_server_url = os.getenv("ADMIN_SERVER_URL", "http://admin.localhost/admin/")
ws_server_url = os.getenv("WS_SERVER_URL", "ws://ws.localhost/ws/")
statics_server_url = os.getenv("STATICS_SERVER_URL", "http://statics.localhost/statics/")
medias_server_url = os.getenv("MEDIAS_SERVER_URL", "http://medias.localhost/medias/")

api_server_name = extract_server_name(api_server_url)
admin_server_name = extract_server_name(admin_server_url)
ws_server_name = extract_server_name(ws_server_url)
statics_server_name = extract_server_name(statics_server_url)
medias_server_name = extract_server_name(medias_server_url)

nginx_config = nginx_template.format(
    api_server_name=api_server_name,
    admin_server_name=admin_server_name,
    ws_server_name=ws_server_name,
    statics_server_name=statics_server_name,
    medias_server_name=medias_server_name
)

with open("nginx_config.conf", "w") as file:
    file.write(nginx_config)
