# celery_tasks
simple django app with celery task and redis 

#download redis and run 


if you are work in windows you can download from this project  :
````
https://github.com/ServiceStack/redis-windows
````

install commands
````
pip install celery
pip install redis

````


run redis server file

activate celery by command (app name is 'tasks')
````
celery -A tasks worker --loglevel=INFO
````