# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings
# install pip
python -m ensurepip --default-pip

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import subprocess
from pathlib import Path
from typing import Dict
from typing import Final
from typing import TypedDict

__all__ = ['EmbedPython']
__version__ = '0.0.1'

BASE = os.path.abspath(os.path.dirname(__file__))
DEFAULT_PYTHON: Final = os.path.abspath(os.path.join(os.path.dirname(__file__), "python310/python.exe"))

logger = logging.getLogger("EmbedPython")
logger.setLevel(logging.WARNING)
logger.propagate = True


class PipSource(TypedDict):
    label: str
    index: str
    url: str


PIP_SOURCES: Dict[str, PipSource] = {
    "pypi": {
        "label": "默认源[官网]",
        "index": "pypi",
        "url": "https://pypi.org/simple",
    },
    "tuna": {
        "label": "清华源[推荐]",
        "index": "tuna",
        "url": "https://pypi.tuna.tsinghua.edu.cn/simple"
    }
}


class EmbedPython:
    def __init__(self, **kwargs):
        self._python_path = kwargs.get('python_path') or DEFAULT_PYTHON
        # version
        self._version = "python310"
        # debug
        if kwargs.get('debug', False):
            logger.setLevel(logging.DEBUG)
            if logging.StreamHandler in [type(handler) for handler in logger.handlers]:
                handler_index = [type(handler) for handler in logger.handlers].index(logging.StreamHandler)
                stream_handler = logger.handlers[handler_index]
            else:
                stream_handler = logging.StreamHandler()
                logger.addHandler(stream_handler)
            stream_handler.setLevel(logging.DEBUG)
        self._debug: bool = kwargs.get('debug', False)
        # env
        self.env = os.environ.copy()
        self.env['PYTHONHOME'] = _path_join(BASE, self._version)
        self.env['PYTHONPATH'] = _path_join(BASE, self._version, 'Lib/site-packages')
        self.env['PATH'] = f"{self._python_env()};{self.env['PATH']}"

    def _python_env(self) -> str:
        return f"{_path_join(BASE, self._version)};{_path_join(BASE, self._version, 'Scripts')}"

    def run(self, *args, **kwargs):
        args = ' '.join(args)
        logger.debug(f"run: {self._python_path} {args}")
        if kwargs.get('test', False):
            return 0
        process = subprocess.Popen(
            f"{self._python_path} {args}",
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            stdin=subprocess.PIPE, shell=True, creationflags=subprocess.CREATE_NO_WINDOW,
            env=self.env
        )
        while True:
            output = process.stdout.read(8)
            if output == b'' and process.poll() is not None:
                break
            if output:
                self.console(output.decode('utf-8'))
        while True:
            output = process.stderr.read(8)
            if output == b'' and process.poll() is not None:
                break
            if output:
                self.console(output.decode('utf-8'))
        rc = process.poll()
        return rc

    def console(self, _a):
        if self._debug:
            print(_a, end='')

    def run_code(self, code: str):
        code = code.strip()
        return self.run(f"-c {code}")

    def pip(self, command, *args, **kwargs):
        """
        pip install -U -t . -i https://pypi.tuna.tsinghua.edu.cn/simple somepackage

        Args:
            command: only support install
            *args: pkg0, pkg1, ..
            **kwargs:

        Returns:

        """
        if command != 'install':
            raise TypeError('command only support install')

        i: str = kwargs.get('i', 'pypi')
        if i.startswith('http'):
            i: tuple = ("-i", i)
        else:
            i: PipSource = PIP_SOURCES.get(i)
            i: str = i['url']
            i: tuple = ("-i", i)

        if kwargs.get('t', None) is None:
            t: tuple = ()
        else:
            t: str = os.path.abspath(kwargs.get('t'))
            if not os.path.exists(t):
                Path(t).mkdir(parents=True)
            t: tuple = ("-t", t)

        pkgs = ','.join(args)

        if kwargs.get('upgrade', False) or kwargs.get('U', False):
            u = ("-U",)
        else:
            u = ()

        args_ = ("-m", 'pip', command, *i, *t, *u, pkgs)

        run_kw = kwargs.copy()
        for k in ['i', 't', 'U', 'upgrade']:
            if k in run_kw.keys():
                del run_kw[k]

        self.run(*args_, **run_kw)


def _path_join(__a, *paths):
    return os.path.abspath(os.path.join(__a, *paths))


def _run_program(cmd):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        stdin=subprocess.PIPE, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
    # 读取输出
    while True:
        output = process.stdout.read(8)
        if output == b'' and process.poll() is not None:
            break
        if output:
            # 将输出以字符串形式打印到控制台
            print(output.decode('utf-8').strip())
    rc = process.poll()
    return rc


def python(*args):
    python_path = os.path.join(os.path.dirname(__file__), "python310/python.exe")
    python_path = os.path.abspath(python_path)
    args = ' '.join(args)
    return subprocess.run(
        f"{python_path} {args}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=subprocess.CREATE_NO_WINDOW
    )


def ensurepip():
    return python("-m ensurepip --default-pip")


def get_pip(**kwargs):
    get_pip_py = _path_join(BASE, "python310", "get-pip.py")
    return EmbedPython(**kwargs).run(get_pip_py)
