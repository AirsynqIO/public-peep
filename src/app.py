from src.core.video import Capture
from src.services import assets


def main():
    assets.init()
    video_proc = Capture(0)
    video_proc.start()


def kafka():
    video_proc = Capture(0)
    video_proc.kafka_stream()


def api_send():
    video_proc = Capture(0)
    video_proc.api_route()


if __name__ == '__main__':
    # main()
    kafka()
    # api_send()
