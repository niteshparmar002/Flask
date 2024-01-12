## Flask

## Install Requirements 
1. pip install Flask-SQLAlchemy
2. pip install mysqlclient
3. pip install celery
4. pip install redis
5. sudo apt-get install redis-server
6. redis-server
7. redis-cli ping
8. sudo service redis-server start
9. sudo apt-get install mysql-server
10. sudo apt-get install libmysqlclient-dev

## Run Celery
1. celery -A app.celery_redis worker --loglevel=info

## Create user in mysql
1. sudo mysql;
2. CREATE USER 'flask'@'localhost' IDENTIFIED BY 'flask';
3. GRANT ALL PRIVILEGES ON *.* TO 'flask'@'localhost' WITH GRANT OPTION;
4. FLUSH PRIVILEGES;

## Create database in mysql
1. create database flask;