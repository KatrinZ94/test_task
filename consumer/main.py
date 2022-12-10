from pika import ConnectionParameters, BlockingConnection

hostname = 'localhost'
port = 5672
queue_name_in = 'inbox_messages'
routing_key_in = 'inbox_messages'

queue_name_out = 'outgoing_messages'
routing_key_out = 'outgoing_messages'

conn_params = ConnectionParameters(hostname, port)
connection = BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue=queue_name_out)


def callback(chanel, method, properties, body):
    channel.basic_publish(exchange='', routing_key=routing_key_out, body=body)


channel.basic_consume(queue_name_in, callback, auto_ack=True)
channel.start_consuming()

