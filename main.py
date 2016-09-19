#!/usr/bin/env python
import pika
from  gpiozero import DigitalOutputDevice

switch =  DigitalOutputDevice(21, initial_value=0)

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'rabbitmq.dev.twleansw.com'))
channel = connection.channel()
channel.queue_declare(queue='remote_power_switch')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    if body == 'POWER_OFF' :
    	switch.on()
    if body == 'POWER_ON' :
    	switch.off()

channel.basic_consume(callback,
                      queue='remote_power_switch',
                      no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()