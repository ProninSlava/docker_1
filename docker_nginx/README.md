Выполните сборку docker образа:

docker build . --tag=my_nginx

Создайте и запустите контейнер из образа:

docker run -d --name nginx -p 80:80 my_nginx