# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from abc import ABC
from abc import abstractmethod
from typing import List
from typing import TypedDict

__all__ = ['BaseFreeWhisperBackend']
__version__ = '0.0.1'


class ModelInfo(TypedDict):
    label: str
    index: str
    description: str


class BaseFreeWhisperBackend(ABC):
    @abstractmethod
    def load(self, model, *args, **kwargs):
        pass

    @abstractmethod
    def available_models(self) -> List[ModelInfo]:
        pass

    @abstractmethod
    def transcribe(self, *args, **kwargs):
        pass


class OpenaiBackend(BaseFreeWhisperBackend):
    def load(self, model, h,*args, **kwargs):
        pass

    def available_models(self):
        pass

    def transcribe(self, model):
        pass
