from kafka import KafkaAdminClient

bs = "b-1.frame-splitter.soibhu.c2.kafka.us-east-2.amazonaws.com:9092,b-2.frame-splitter.soibhu.c2.kafka.us-east-2.amazonaws.com:9092"
kadmin = KafkaAdminClient(bootstrap_servers=bs, request_timeout_ms=100000, api_version=(0, 11, 5))

res = kadmin.create_topics(["camera-split-images"])
print(res)