# CTS-Kafka-Presentation
Demo for presentation made at the Cygni Tech Summit 2021

Below are instructions for how to get the demo started and running on your own machine

### Requirements:
This is what was used to run the demo on, other versions might work but no guarentees.

- Python 2.7
- Java 11
- Node v12.13.0
- Docker
- Google Maps API-key (For frontend app https://developers.google.com/maps/documentation/javascript/get-api-key)

## Steps to run:
- **Start a local Kafka cluster using Docker.**
   In the demo i used a docker image from Lenses.io (https://github.com/lensesio/fast-data-dev). It creates a Kafka cluster with all the needed things. See below command for how to start it. The Docker image also comes with a web UI so you can see that it is running correctly and browse your topics for example. Go to http://localhost:3030 to browse it.


```
  docker run --rm -p 2181:2181 -p 3030:3030 -p 8081-8083:8081-8083 -p 9581-9585:9581-9585 -p 9092:9092 -e ADV_HOST=localhost -e SAMPLEDATA=0 lensesio/fast-data-dev:latest
```

- **Create topic inside the Kafka cluster**
  For this i used the bitnami docker image in order to be able to create a topic through their CLI. This could also be installed locally, you could also utilize for example Kafkacat
```
docker run --net=host --rm -it -v my-vol:/app bitnami/kafka:2 /bin/bash

Then run the following the command:

/opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic cts-topic --if-not-exists --partitions 3
```
- **Start the frontend app**
Remember to set the Google Maps API-key as an environment variable. Make sure you have Node installed. You need to be in the correct directory to run the below command.
```
yarn start
```
- **Start the consumer app** 
Make sure you have atleast Java 11 installed. You need to be in the correct directory to run the below command.
```
./gradlew bootRun
```
- **Write messages to Kafka topic** 
Make sure you have Python 2.7 installed. You need to be in the correct directory to run the below command.
```
pip install kafka-python 
python kafka-producer.py
```

With the above commands you should be able to see the data being received in the Consumer app and also the aeroplanes flying in the frontend app. 

