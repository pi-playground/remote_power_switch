#!/usr/bin/env python
import pika
from  gpiozero import DigitalOutputDevice

switch =  DigitalOutputDevice(21, initial_value=0 ,active_high=False )

while True :
    connection = pika.BlockingConnection(pika.ConnectionParameters(
                   'rabbitmq.dev.twleansw.com'))
    channel = connection.channel()
    channel.queue_declare(queue='remote_power_switch')
    poserStatus = 'POWER_STATUS_OFF'
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        if body == 'POWER_OFF' :
        	switch.off()
        	poserStatus = 'POWER_STATUS_ON'
        if body == 'POWER_ON' :
        	switch.on()
        	poserStatus = 'POWER_STATUS_OFF'
        if body == 'REPORT_STATUS' :
        	channel.basic_publish(exchange='',
    	                      routing_key='remote_power_status_report',
    	                      body= poserStatus)

    channel.basic_consume(callback,
                          queue='remote_power_switch',
                          no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    finally:
        connection.close()
