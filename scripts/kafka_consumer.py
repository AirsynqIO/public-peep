# consumer is only used for test purposes. Please ignore

# import cv2
# import numpy as np
# from kafka import KafkaConsumer
# import datetime
# from src.services.assets import asset_path, init
#
# init()
#
# """
# /usr/local/kafka-server"""
#
# images_topic = "camera-split-images"
#
# KAFKA_SERVER = "18.219.242.102:9092"
#
# images = KafkaConsumer(images_topic,
#                        bootstrap_servers=KAFKA_SERVER,
#                        group_id="local_model_consumer")
#
# for image in images:
#     print(image)
#     nparr = np.fromstring(image.value, np.uint8)
#     imp_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     filename = f"kafka-{datetime.datetime.now().isoformat()}.jpg"
#     filepath = asset_path(filename)
#     print(filepath)
#     cv2.imwrite(filepath, imp_np)


from kafka import KafkaConsumer

topic = "unique-topic-name"

consumer = KafkaConsumer(topic, bootstrap_servers="18.223.28.14:9092", group_id="please_work")

for data in consumer:
    print(data)

