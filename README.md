## elastic stack

### elasticserach 7.6.2

- download: https://www.elastic.co/cn/downloads/past-releases/elasticsearch-7-6-2
- https://www.elastic.co/guide/en/elasticsearch/reference/7.9/targz.html

https://www.elastic.co/guide/en/elasticsearch/reference/6.5/search.html

-->Congfiguration
1. config/elasticsearch.yml
cluster.name: rachelpoc
node.name: rachelpoc-node-1
path.data: /Users/liuruiqin1/poc/elasticsearch-7.6.2/data
path.logs: /Users/liuruiqin1/poc/elasticsearch-7.6.2/logs
network.host: localhost 
http.port: 9200

2. add the JAVA HOME to ~/.config/fish/config.fish 
set -x JAVA_HOME /Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home


### kibana 7.6

https://www.elastic.co/guide/en/kibana/7.6/targz.html

https://www.elastic.co/guide/en/kibana/current/index.html
-->Configuration
config.kinana.yml
server.port: 5601
server.host: "localhost"

server.name: "rachelpoc"
elasticsearch.hosts: ["http://localhost:9200"]
elasticsearch.preserveHost: true

kibana.index: ".kibana"

### logstash

https://www.elastic.co/guide/en/logstash/7.x/index.html

https://www.elastic.co/guide/en/logstash/7.x/plugins-inputs-kafka.html

-->CONFIG:also check java version add the JAVA HOME

## Kafka

https://kafka.apache.org/quickstart
--> Configuration
1. zookeeper.properties
dataDir=/Users/liuruiqin1/poc/test-data/zookeeper
clientPort=2181
maxClientCnxns=0
admin.enableServer=false
2. server.properties
( if we have multipe server, we can use nohup to bg start several severs with diff server properties
------->https://kafka.apache.org/24/documentation.html#consumerconfigs)
log.dirs=/Users/liuruiqin1/poc/test-data/kakfa-logs


bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-server-start.sh config/server.properties

#create the topic(describe -->bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092)
bin/kafka-topics.sh --create --topic rachelpoc-collectlog-v1 --bootstrap-server localhost:9092

https://riccomini.name/how-paint-bike-shed-kafka-topic-naming-conventions<F2>

##### E2E
https://www.devglan.com/apache-kafka/kafka-elasticsearch-logstash-example
https://medium.com/inside-freenow/centralized-logs-with-elastic-stack-and-apache-kafka-7db576044fe7


# Startup

1. elasticsearch-7.6.2]$ ./bin/elasticsearch -d -p pid  (to stop ES: pkill -F pid)
2. postman: http://localhost:9200/
3. kafka_2.13-2.6.0]$ ./bin/zookeeper-server-start.sh config/zookeeper.properties (telnet localhost 2181)
4. kafka_2.13-2.6.0]$ ./bin/kafka-server-start.sh config/server.properties (telnet localhost 9092)
5. kibana-7.6.2-darwin-x86_64]$ bin/kibana  (http://localhost:5601)
6. logstash-7.6.2]$ ./bin/logstash -f rachelpoc-collectlog-v1.conf
7. kafka_2.13-2.6.0]$ bin/kafka-console-producer.sh --topic rachelpoc-collectlog-v1 --bootstrap-server localhost:9092 
8. check consumer:bin/kafka-console-consumer.sh  --topic rachelpoc-collectlog --bootstrap-server localhost:9092


> https://support.apple.com/zh-cn/HT202491

$ bin/kafka-topics.sh  --zookeeper localhost:2181 --topic rachel-collectlog-v1 --delete
Topic rachel-collectlog-v1 is marked for deletion.
Note: This will have no impact if delete.topic.enable is not set to true.
[liuruiqin1@liuruiqindeMacBook-Pro ~/poc/kafka_2.13-2.6.0]$ bin/kafka-topics.sh --list --zookeeper localhost:2181
