from kafka import KafkaProducer

from src.config import RPI_ASSIGNED_ID

imagesProducer = KafkaProducer(bootstrap_servers="3.14.84.232:9092")
images_topic = "camera-split-images"


def send_image(frame):
    # todo: location data will be updated later
    data = {'frame': frame, 'location': {}, 'assigned_id': RPI_ASSIGNED_ID}
    imagesProducer.send(images_topic, data)
    imagesProducer.flush()
