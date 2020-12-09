kafka_instance = "i-07154d11d45901391"

# /home/ubuntu/odin/venv/bin/gunicorn

import json

from kafka import KafkaProducer

predictionsProducer = KafkaProducer(bootstrap_servers="18.223.28.14:9092")
prediction_topic = "predictions"

sample_predictions = [
    {
        "classes": [
            "person",
            "Car",
            "Bus",
            "Skater"
        ],
        "image": "https://modeltraindetection.s3.us-east-2.amazonaws.com/result/image-2020-12-08T11:09:11.788368.jpg",
        "message": True,
        "status": "success",
        "threat": 30
    }
]

for pred in sample_predictions:
    val = json.dumps(pred).encode()
    print(val)
    res = predictionsProducer.send(prediction_topic, val)
    print(res)
    predictionsProducer.flush()