from src.core.video import Capture
from src.services import assets


def main():
    assets.init()
    video_proc = Capture(0)
    video_proc.start()


if __name__ == '__main__':
    main()
