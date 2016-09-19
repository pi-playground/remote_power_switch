#!/usr/bin/env python
import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters(
               'rabbitmq.dev.twleansw.com'))
channel = connection.channel()
for i in range(0, 2) :
	channel.queue_declare(queue='remote_power_switch')
	channel.basic_publish(exchange='',
	                      routing_key='remote_power_switch',
	                      body='POWER_ON')
	print(" [x] Sent POWER_ON")
	time.sleep(5) # delays for 5 seconds
	
	channel.queue_declare(queue='remote_power_switch')
	channel.basic_publish(exchange='',
	                      routing_key='remote_power_switch',
	                      body='POWER_OFF')
	time.sleep(5) # delays for 5 seconds
	print(" [x] Sent POWER_OFF")

