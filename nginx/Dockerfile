FROM nginx:latest

RUN mkdir /certs

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf.template /etc/nginx/templates/