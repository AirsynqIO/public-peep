# consumer is only used for test purposes. Please ignore

import cv2
import numpy as np
from kafka import KafkaConsumer
import datetime
from src.services.assets import asset_path, init

init()

images_topic = "camera-split-images"

KAFKA_SERVER = "18.219.242.102:9092"

images = KafkaConsumer(images_topic,
                       bootstrap_servers=KAFKA_SERVER,
                       group_id="local_model_consumer")

for image in images:
    print(image)
    nparr = np.fromstring(image.value, np.uint8)
    imp_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    filename = f"kafka-{datetime.datetime.now().isoformat()}.jpg"
    filepath = asset_path(filename)
    print(filepath)
    cv2.imwrite(filepath, imp_np)
