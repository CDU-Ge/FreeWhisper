# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import io
os.environ['PYTHONUTF8'] = '1'

from moviepy.video.tools.subtitles import SubtitlesClip

os.environ['IMAGEMAGICK_BINARY'] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

import pysrt
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip



def main():
    video_path = r"H:\DATASETS\Animes\jlh1000.mp4"
    srt_path = r"H:\DATASETS\Animes\jlh1000.srt"
    output_path = r"H:\DATASETS\Animes\[合成]jlh1000.mp4"

    video_clip = VideoFileClip(video_path)
    pysrt.open(srt_path, encoding='utf-8').save(srt_path, encoding='utf-8')
    subtitle_clip = SubtitlesClip(srt_path)
    subtitle_clip = subtitle_clip.set_position(('center', 'bottom'))

    video_with_subtitles = CompositeVideoClip([video_clip, subtitle_clip])
    video_with_subtitles.write_videofile(output_path, fps=video_clip.fps, codec='libx264', audio_codec='aac'
                            )


if __name__ == '__main__':
    main()
