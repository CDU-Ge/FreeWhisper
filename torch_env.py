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
import re
import subprocess
import sys
from typing import List
from typing import Literal


def torch_env(home: str = None) -> str:
    home = home if home else os.environ.get('CUDA_PATH_PROJECT')
    _bin = os.path.join(home, 'bin')
    _libnvvp = os.path.join(home, 'libnvvp')
    return ';'.join(map(os.path.abspath, [_bin, _libnvvp]))


TORCH_VERSION = {
    "release": {
        "cpu": "install torch torchvision torchaudio",
        "cu117": "install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117",
        "cu118": "install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118",
    },
    "1.13.1": {
        "cpu": "install torch==1.13.1+cpu torchvision==0.14.1+cpu torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cpu",
        "cu116": "install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116",
        "cu117": "install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117"
    }
}


def get_cuda_version():
    """
    Get CUDA version by system.

    Returns:
        str: nvcc version
    """
    startupinfo = None
    if sys.platform == 'win32':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE

    try:
        result = subprocess.check_output(["nvcc", "-V"], stderr=subprocess.STDOUT, startupinfo=startupinfo, text=True,
                                         encoding='utf-8')
        version_match = re.search(r"release (\d+\.\d+)", result)
        if version_match:
            return version_match.group(1).strip()
        else:
            return ''
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ''


def get_platform() -> Literal['cpu', 'cuda']:
    """

    Returns:
        str: platform name, cpu or cuda version
    """
    cuda_version = get_cuda_version()
    if cuda_version:
        return 'cuda'
    else:
        return 'cpu'


def get_torch_install_cmd(version='release', platform=None, cuda_version=None) -> List[str]:
    """
    get install cmd for torch.

    Args:
        version: torch version, only support: "release", "1.13.1"
        platform: auto select when CUDA be used. It fource get value.
        cuda_version: CUDA version

    Returns:
        pip cmd
    """
    torch_version = TORCH_VERSION.get(version, TORCH_VERSION.get('release'))
    platform = platform or get_platform()
    if platform == 'cpu':
        return torch_version.get('cpu').split()
    else:
        cuda_version = cuda_version or get_cuda_version()
        if not cuda_version:
            return torch_version.get('cpu').split()
        cuda_version = cuda_version.replace('.', '')
        cuda_version = f"cu{cuda_version}"
        if cuda_version not in torch_version.keys():
            return torch_version.get('cpu').split()
        else:
            return torch_version.get(cuda_version).split()
