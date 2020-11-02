import cv2
import datetime
from src.services.assets import asset_path


# todo: function accepts param which is passed to video capture
# todo: frames are sent via api (async jobs) based on fps
class Capture:

    def __init__(self, capture_param):
        self.capture_param = capture_param

    def start(self):
        cap = cv2.VideoCapture(self.capture_param)
        print(f"Captured {self.capture_param}")
        fps = round(cap.get(cv2.CAP_PROP_FPS))
        print(f"FPS: {fps}")

        if not cap.isOpened():
            raise IOError("Cannot open video capture")

        frame_count = fps
        while True:
            print(f"Frame count: [{frame_count}]")
            ret, frame = cap.read()
            print(f"Image capture: {ret}")

            if frame_count == 0:
                filename = f"image-{datetime.datetime.now().isoformat()}.jpg"
                cv2.imwrite(asset_path(filename), frame)
                frame_count = fps
            else:
                frame_count -= 1
