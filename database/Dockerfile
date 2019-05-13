FROM mysql:latest

ENV MYSQL_ROOT_USERNAME=root
ENV MYSQL_ROOT_PASSWORD=root
COPY init.sql /docker-entrypoint-initdb.d
