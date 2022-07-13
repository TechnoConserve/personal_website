FROM nginx:latest

RUN apt update
RUN apt install -y python3 python3-venv libaugeas0
RUN python3 -m venv /opt/certbot/
RUN /opt/certbot/bin/pip install --upgrade pip
RUN /opt/certbot/bin/pip install certbot certbot-nginx
RUN ln -s /opt/certbot/bin/certbot /usr/bin/certbot
RUN certbot certonly --nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf.template /etc/nginx/templates/
