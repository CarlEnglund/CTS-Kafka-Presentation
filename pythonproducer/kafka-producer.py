from kafka import KafkaProducer
import time
import json

firstPlane = [{ 'lon': 18,
        'lat': 59},{ 'lon': 22,
        'lat': 47},{ 'lon': 22,
        'lat': 45},{ 'lon': 15,
        'lat': 43},{ 'lon': 23,
        'lat': 41},{ 'lon': 14,
        'lat': 37}]

secondPlane = [{ 'lon': 25,
        'lat': 47},{ 'lon': 24,
        'lat': 45},{ 'lon': 23,
        'lat': 45},{ 'lon': 12,
        'lat': 43},{ 'lon': 21,
        'lat': 41},{ 'lon': 20,
        'lat': 37}]
        
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for index in firstPlane:
  producer.send(topic='cts-topic',
                key='XYZ',
                value=json.dumps(index))
  time.sleep(1)

for index in secondPlane:
  producer.send(topic='cts-topic',
                key='ABC',
                value=json.dumps(index))
  time.sleep(1)
producer.flush()
