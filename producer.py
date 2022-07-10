import pika

credentials = pika.PlainCredentials('user', 'user1234')
connection_param = pika.ConnectionParameters(
    "localhost", credentials=credentials)
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

channel.queue_declare("log_queue")

log = "Hello this is a log"

channel.basic_publish(exchange="", routing_key='log_queue', body=log)

print("Message sent", log)

connection.close()
