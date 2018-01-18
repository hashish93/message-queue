from huey.contrib.djhuey import task
from .redisConfig import RedisWrapper
import json

@task()
def pushNotification(obj):
    response_data = {}
    response_data['msg'] = obj['message']
    response_data['toIds'] = obj['user_ids'],
    response_data['broadcast'] = 1 if obj['broadcast'] else 0
    print(response_data)
    try:
        r_server = RedisWrapper().redis_connect(server_key='local_server')
        r_server.ping()
        r_server.publish('notification', json.dumps(response_data))
    except Exception:
        print('cannot connect to redis server')
        print(Exception)
