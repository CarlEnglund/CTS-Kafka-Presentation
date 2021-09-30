from kafka import KafkaProducer
import time
import json

firstPlane = [ 
        { 'lon': 17,'lat': 58},
        { 'lon': 17,'lat': 56},
        { 'lon': 16,'lat': 55},
        { 'lon': 15,'lat': 54},
        { 'lon': 14,'lat': 53},
        { 'lon': 13,'lat': 52},
        { 'lon': 12,'lat': 48},
        { 'lon': 13,'lat': 47}]      

secondPlane = [ 
        { 'lon': 11,'lat': 57},
        { 'lon': 9,'lat': 56},
        { 'lon': 7,'lat': 56},
        { 'lon': 6,'lat': 54},
        { 'lon': 5,'lat': 54},
        { 'lon': 3,'lat': 53},
        { 'lon': 2,'lat': 52},
        { 'lon': 0,'lat': 51}]  
        
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for index in firstPlane:
  producer.send(topic='cts-topic',
                key='ABC',
                value=json.dumps(index))
  time.sleep(1)

for index in secondPlane:
  producer.send(topic='cts-topic',
                key='XYZ',
                value=json.dumps(index))
  time.sleep(1)

"""for index in reversed(firstPlane):
  producer.send(topic='cts-topic',
                key='ABC',
                value=json.dumps(index))
  time.sleep(1)

for index in reversed(secondPlane):
  producer.send(topic='cts-topic',
                key='XYZ',
                value=json.dumps(index))
  time.sleep(1) """ 
