sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo nginx -s reload

gunicorn --bind='0.0.0.0:8080' hello:app