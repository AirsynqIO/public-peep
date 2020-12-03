import cv2
import imutils
import datetime
from src.services.assets import asset_path
from src.core.kafka_producer import send_image
from src.services.api import send_file_async


# todo: frames are sent via api (async jobs) based on fps
class Capture:

    def __init__(self, capture_param):
        self.capture_param = capture_param

    def view(self):
        cap = cv2.VideoCapture(self.capture_param)
        while True:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def api_route(self):
        cap = cv2.VideoCapture(self.capture_param)
        print(f"Captured {self.capture_param}")
        fps = 24
        print(f"FPS: {fps}")

        if not cap.isOpened():
            raise IOError("Cannot open video capture")

        frame_count = fps
        while True:
            ret, frame = cap.read()
            print(f"Frame count: [{frame_count}] || Image capture: {ret}")

            if frame_count == 0:
                filename = f"image-{datetime.datetime.now().isoformat()}.jpg"
                filepath = asset_path(filename)
                cv2.imwrite(filepath, frame)
                send_file_async(filepath)
                frame_count = fps
            else:
                frame_count -= 1

    def kafka_stream(self):
        cap = cv2.VideoCapture(self.capture_param)
        print(f"Captured {self.capture_param}")
        fps = round(cap.get(cv2.CAP_PROP_FPS))
        print(f"FPS: {fps}")

        if not cap.isOpened():
            raise IOError("Cannot open video capture")

        frame_count = fps
        while True:
            ret, frame = cap.read()
            print(f"Frame count: [{frame_count}] || Image capture: {ret}")

            if frame_count == 0:
                image = imutils.resize(frame, width=400)
                send_image(cv2.imencode('.jpg', image)[1].tobytes())
                frame_count = fps
            else:
                frame_count -= 1

    def start(self):
        cap = cv2.VideoCapture(self.capture_param)
        print(f"Captured {self.capture_param}")
        fps = 24
        print(f"FPS: {fps}")

        if not cap.isOpened():
            raise IOError("Cannot open video capture")

        frame_count = fps
        while True:
            ret, frame = cap.read()
            print(f"Frame count: [{frame_count}] || Image capture: {ret}")

            if frame_count == 0:
                filename = f"image-{datetime.datetime.now().isoformat()}.jpg"
                cv2.imwrite(asset_path(filename), frame)
                frame_count = fps
            else:
                frame_count -= 1
