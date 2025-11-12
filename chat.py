import redis
import json

REDIS_HOST = 'de.futoke.ru'
REDIS_PORT = 6379
PIPE_NAME = 'itmo'


def init_chat():
    conn = redis.StrictRedis(host=REDIS_HOST,
                      port=REDIS_PORT,
                      db=0,
                      username='default',
                      password='itmoredis',
                      decode_responses=True)
    reader = conn.pubsub()
    reader.subscribe(PIPE_NAME)
    return conn, reader

def send_msg(msg, conn):
    conn.publish(PIPE_NAME, json.dumps(msg))

def read_msgs(callback, reader, frame_msgs):
    for msg in reader.listen():
        if type(msg['data']) is int:
            continue
        msg = json.loads(msg['data'])
        callback(frame_msgs, 
                 f'{msg["nickname"]}:\n{msg["text"]}')

conn, reader = init_chat()
