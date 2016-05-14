# sudo rm /etc/nginx/sites-enabled/default
sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hallo.py   /etc/gunicorn.d/hallo.py
sudo /etc/init.d/gunicorn restart
