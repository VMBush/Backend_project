sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart

cd ask
gunicorn --bind='0.0.0.0:8000' ask.wsgi:application