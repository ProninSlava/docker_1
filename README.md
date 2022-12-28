weapon_api

Для создания docker-образа перейти в директорию weapon_api и выполнить команду

docker build -t rest_api .
Для запуска контейнера

docker run -d -p 7500:80 rest_api