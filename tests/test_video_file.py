import os.path
import unittest

from moviepy.video.io.VideoFileClip import VideoFileClip

from myconf import TEST_VIDEO_PATH
from myconf import output_file


class MyTestCase(unittest.TestCase):
    def test_save_audio(self):
        output_file_path = output_file('output', 'mp3')
        video_file = TEST_VIDEO_PATH
        video = VideoFileClip(video_file)
        video.audio.write_audiofile(output_file_path)
        self.assertTrue(os.path.exists(output_file_path))  # add assertion here


if __name__ == '__main__':
    unittest.main()
