from kafka import KafkaProducer

zookeeper_connect_string = "z-3.frame-splitter.soibhu.c2.kafka.us-east-2.amazonaws.com:2181,z-2.frame-splitter.soibhu.c2.kafka.us-east-2.amazonaws.com:2181,z-1.frame-splitter.soibhu.c2.kafka.us-east-2.amazonaws.com:2181"


imagesProducer = KafkaProducer(bootstrap_servers="localhost:9092")
images_topic = "camera-split-images"


def send_image(frame):
    imagesProducer.send(images_topic, frame)
