# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from moviepy.editor import VideoFileClip


def get_fps():
    video = VideoFileClip(r"H:\DATASETS\Animes\jlh1000.mp4")
    return video.fps


print(get_fps())
