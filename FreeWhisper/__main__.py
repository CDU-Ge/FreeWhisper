# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import os
import pprint
import sys
from pathlib import Path
from typing import Final

import dotenv
import yaml

from torch_env import torch_env
from FreeWhisper.gui import launch_gui

ROOT: Final = Path(__file__).parent.absolute()
SUPPORT_LANGUAGE = None


def get_logger():
    Path('.cache').mkdir(exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler('.cache/free_whisper.log', encoding='utf8')
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


logger = get_logger()


def get_parser():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    subparser_test = subparser.add_parser('test')
    subparser_test.add_argument('--config')
    subparser_test.add_argument('-f', '--format', dest='is_format',
                                action='store_true', required=False)

    return parser


def init_env(**kwargs):
    if dotenv_path := kwargs.get('env_path'):
        dotenv.load_dotenv(dotenv_path)
    os.environ['Path'] = f"{torch_env()};" + os.environ['Path']


def fullpath(config_path: str) -> str:
    if not os.path.abspath(config_path):
        return os.path.abspath(config_path)
    return config_path


def load_config(config_path):
    config_path = fullpath(config_path)
    if not os.path.isfile(config_path):
        logger.warning('file not find or path is not a file')
        return None
    return yaml.safe_load(Path(config_path).read_text(encoding='utf8'))


def _test(argv: argparse.Namespace):
    argv.config = fullpath(argv.config)
    config: dict = load_config(argv.config)
    if argv.is_format:
        config['widgets'] = [os.path.abspath(src) for src in config.get('widgets', [])]
        with open(argv.config, 'w', encoding='utf8') as f:
            logger.info(f'write to {argv.config}')
            yaml.safe_dump(config, f)
    pprint.pprint(config)


def main(argv):
    logger.info(f'argv: {argv}')
    parser = get_parser()
    argv_ = parser.parse_args(argv[1:])
    logger.info(argv_)
    if argv_.command == 'test':
        _test(argv_)
    else:
        launch_gui(argv)


if __name__ == '__main__':
    main(sys.argv)
