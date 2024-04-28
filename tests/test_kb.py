# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""
from pynput import keyboard

def on_press(key):
    print('{0} pressed'.format(key))

def on_release(key):
    print('{0} release'.format(key))

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()