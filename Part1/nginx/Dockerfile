FROM nginx:latest

RUN apt-get update \  
 && apt-get install -y -q --no-install-recommends \
    ca-certificates \
    wget \
 && apt-get clean \
 && rm -r /var/lib/apt/lists/*

# Add main NGINX config
RUN rm -f /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/ssl
COPY ssl/ /etc/nginx/ssl
COPY nginx.conf /etc/nginx/

COPY web.conf /etc/nginx/conf.d
