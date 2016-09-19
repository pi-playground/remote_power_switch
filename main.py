#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'rabbitmq.dev.twleansw.com'))
channel = connection.channel()
channel.queue_declare(queue='remote_power_switch')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    if body == 'Hello World!' :
    	print('Got Hello World!')

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()