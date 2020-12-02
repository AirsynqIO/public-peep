from src.core.video import Capture
from src.services import assets

captureSet = "gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, framerate=24/1 ! videoconvert ! autovideosink"


def main():
    assets.init()
    video_proc = Capture(0)
    video_proc.start()


def show():
    video_proc = Capture(0)
    video_proc.view()


if __name__ == '__main__':
    # main()
    show()
