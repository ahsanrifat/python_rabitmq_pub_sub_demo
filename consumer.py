import pika


def on_log_received(ch, method, properties, body):
    print("Message Received----->", body)


credentials = pika.PlainCredentials('user', 'user1234')
connection_param = pika.ConnectionParameters(
    "localhost", credentials=credentials)
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

channel.queue_declare("log_queue")

channel.basic_consume(queue="log_queue", auto_ack=True,
                      on_message_callback=on_log_received)

print("Started Consuming====================>>>>")

channel.start_consuming()
