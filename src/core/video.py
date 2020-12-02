import cv2
import datetime
from src.services.assets import asset_path


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

    def start(self):
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
                filename = f"image-{datetime.datetime.now().isoformat()}.jpg"
                cv2.imwrite(asset_path(filename), frame)
                frame_count = fps
            else:
                frame_count -= 1
