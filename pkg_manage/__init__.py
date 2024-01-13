# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import importlib
import os
from functools import wraps
from typing import Callable
from typing import List
from typing import Literal
from typing import Optional
from typing import Type

commands = [
    ('install', 'Install packages.'),
    ('download', 'Download packages.'),
    ('uninstall', 'Uninstall packages.'),
    ('freeze', 'Output installed packages in requirements format.'),
    ('inspect', 'Inspect the python environment.'),
    ('list', 'List installed packages.'),
    ('show', 'Show information about installed packages.'),
    ('check', 'Verify installed packages have compatible dependencies.'),
    ('config', 'Manage local and global configuration.'),
    ('search', 'Search PyPI for packages.'),
    ('cache', "Inspect and manage pip's wheel cache."),
    ('index', 'Inspect information available from package indexes.'),
    ('wheel', 'Build wheels from your requirements.'),
    ('hash', 'Compute hashes of package archives.'),
    ('completion', 'A helper command used for command completion.'),
    ('debug', 'Show information useful for debugging.'),
    ('help', 'Show help for commands.')
]

COMMANDS = Literal[
    'install',
    'download',
    'uninstall',
    'freeze',
    'inspect',
    'list',
    'show',
    'check',
    'config',
    'search',
    'cache',
    'index',
    'wheel',
    'hash',
    'completion',
    'debug',
    'help'
]
"""pip commands"""


def not_exit(fun):
    @wraps(fun)
    def _inner(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except SystemExit:
            pass

    return _inner


@not_exit
def pip(*args: str) -> int:
    args = args if args else None
    pip = importlib.import_module('pip._internal.cli.main')
    pip_cli = getattr(pip, 'main', pip)
    pip_cli: Callable[[Optional[List[str]]], ...]
    return pip_cli(list(args))

# TODO: 添加install接口
# TODO: 单元测试
# TODO: 集成测试
# TODO: 增加模块 pkg，为下类添加别名
class PackageManage:
    """
    管理第三方包

    Attributes:
        root: 项目、软件根目录
    """

    def __init__(self, root: str = None):
        """

        init

        Args:
            root: root path
                值缺省时或为`None`时，root默认为`os.getcwd()`，为文件时为该文件所在目录。
                当目录或文件不存在时，会自行创建对应文件夹且不做安全校验。
                指定包下载路径，将会下载在root路径下的`libs`目录。
                建议在 `main` 中使用 `__file__`。
                **会自行将该目录添加到搜索路径末尾**
        """
        self.root = root

    def set_root(self, root: Optional[str]):
        """

        Args:
            root:
                值缺省时或为`None`时，root默认为`os.getcwd()`，为文件时为该文件所在目录。
                当目录或文件不存在时，会自行创建对应文件夹且不做安全校验。
                指定包下载路径，将会下载在root路径下的`libs`目录。
                建议在 `main` 中使用 `__file__`。
                **会自行将该目录添加到搜索路径末尾**

        Returns:
            PackageManage: xxx
        """

    def install(self, cmd: List[str], target: Optional[str] = None) -> 'PackageManage':
        if cmd and cmd[0] == 'install':
            cmd = cmd[:]
        else:
            cmd = ['install'] + cmd[:]
        if target:
            cmd.append('-t')
            cmd.append(os.path.abspath(os.path.join()))
        pip()
        return cls
