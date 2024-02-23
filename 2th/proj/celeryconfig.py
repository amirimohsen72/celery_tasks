broker_url='redis://localhost:6379'
result_backend ='redis://localhost:6379/'
task_serializer='json'
accept_content=['json']
result_serializer='json'
timezone='Asia/tehran'
enable_utc=True
include=['proj.tasks']

task_default_queue = 'queue1'
task_routes = {
    'proj.tasks.add' : {'queue' : 'queue1'},
    'proj.tasks.devide' : {'queue' : 'queue2'},
    'proj.tasks.average' : {'queue' : 'queue3'},
}