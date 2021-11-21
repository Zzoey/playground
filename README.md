__Part 2 :)__
- __`unified_api.py`__ - Contains a class for the unified api an argument as a string
- __`unified_api_publisher.py`__ - Driver script to use the __unified_api__ and as a publisher you can select __kafka__ service or __pubsub__ service by passing it as an argument
- __`unified_api_subscriber.py`__ - Driver script to use the __unified_api__ and as a subscriber you can select __kafka__ service or __pubsub__ service by passing it as an argument
- __`config_copy.py`__ - Copy the contents of this file and create a new file called __config.py__ and add your respective paths to private keys, topic paths and subscription paths

-  __utils__ - This folder contains publisher and subscriber classes for both pubsub and kafka services 
   - __`apache_kafka.py`__ - Contains a class for kafka publisher and kafka subscriber
   - __`google_pub_sub.py`__ - Contains a class for gcp publisher and gcp subscriber

- __test__ - This folder contains publisher and subscriber tests for both pubsub and kafka services
  - __`gcp_publisher.py`__ - Driver script to test pubsub publisher
  - __`gcp_subscriber.py`__ - Driver script to test pubsub subscriber
  - __`kafka_publisher.py`__ - Driver script to test kafka publisher
  - __`kafka_subscriber.py`__ - Driver script to test kafka subscriber

### Installation

1. ```virtualenv -p python3 venv```
2. ```source venv/bin/activate```
3. ```pip install -r requirements.txt```
#### For Kafka
4. Install Kafka and Zookeeper and have them both running in seperate terminals
   - After downloading kafka from https://kafka.apache.org/downloads into /opt/, unzip it.
   - go to config/server.properties and edit (uncomment) the following lines by adding your local ip or localhost
      - ```advertised.listeners=PLAINTEXT://[server-ip-address]:9092```
      - ```zookeeper.connect=localhost:2181```
5. start zookeeper by running 
   - ```bin/zookeeper-server-start.sh config/zookeeper.properties```
6. Open another terminal and start the kafka server
   - ```JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties```
#### For Google Pub/Sub
7. Go to GCP, create a project, enable pubsub for that project
8. Create a topic, subscription for that project
9. Create a key that private key is to be used for authenticating your publisher and subscriber

### Running

1. open a terminal, and run ```python unified_api_subscriber.py --api_type kafka``` to use kafka
2. open another terminal, and run ```python unified_api_publisher.py --api_type kafka``` and you will be able to see the the message in the previous terminal
3. All of this is done while keeping the zookeeper and kafka running
4. You can use pubsub just adding the argument as ```python unified_api_subscriber.py --api_type pubsub``` for both publisher and subscriber

### Note

- Developed on ubuntu 18.04
- This api is as unified as possible, with help of one argument you can switch between two services





