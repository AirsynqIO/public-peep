from kafka import KafkaProducer

imagesProducer = KafkaProducer(bootstrap_servers="13.14.84.232:9092")
images_topic = "camera-split-images"


def send_image(frame):
    imagesProducer.send(images_topic, frame)
