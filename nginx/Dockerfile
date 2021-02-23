FROM nginx

WORKDIR /var/www/html

COPY ./index.html ./

CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]
