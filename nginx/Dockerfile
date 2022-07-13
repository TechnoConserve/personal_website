FROM nginx:latest

RUN apt update && apt install -y snapd
RUN snap install core; sudo snap refresh core
RUN snap install --classic certbot
RUN ln -s /snap/bin/certbot /usr/bin/certbot
RUN certbot certonly --nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf.template /etc/nginx/templates/
