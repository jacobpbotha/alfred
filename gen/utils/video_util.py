import subprocess

from .. import constants


class VideoSaver(object):
    def __init__(self, frame_rate=constants.VIDEO_FRAME_RATE):
        self.frame_rate = frame_rate

    def save(self, image_path, save_path):
        subprocess.call(
            [
                f"ffmpeg -r {self.frame_rate} -pattern_type glob -y -i '{image_path}' -c:v libx264 -pix_fmt yuv420p '{save_path}'"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=True,
        )
