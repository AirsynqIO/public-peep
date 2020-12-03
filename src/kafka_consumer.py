# consumer is only used for test purposes. Please ignore

import cv2
import numpy as np
from kafka import KafkaConsumer
import datetime
from src.services.assets import asset_path

images_topic = "camera-split-images"

images = KafkaConsumer(images_topic,
                       bootstrap_servers="localhost:9092",
                       group_id="webcam_images_consumer")

for image in images:
    print(image)
    nparr = np.fromstring(image.value, np.uint8)
    imp_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    filename = f"kafka-{datetime.datetime.now().isoformat()}.jpg"
    cv2.imwrite(asset_path(filename), imp_np)
