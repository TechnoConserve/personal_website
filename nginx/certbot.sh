#/bin/sh

certbot certonly \
    --agree-tos \
    --non-interactive \
    -m uslaner.avery@gmail.com \
    --dns-digitalocean \
    --dns-digitalocean-credentials /digitalocean.ini \
    -d averyuslaner.com 