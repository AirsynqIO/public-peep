from kafka import KafkaProducer
import json

from src.config import RPI_ASSIGNED_ID

imagesProducer = KafkaProducer(bootstrap_servers="3.137.195.2:9092")
images_topic = "camera-split-images"


def send_image(frame):
    # todo: location data will be updated later
    meta_data = {'location': {}, 'assigned_id': RPI_ASSIGNED_ID}
    imagesProducer.send(images_topic, value=frame, key=json.dumps(meta_data).encode())
    imagesProducer.flush()
