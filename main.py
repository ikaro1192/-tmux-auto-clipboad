#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import commands
import os

def get_now_tmux_buffer():
    return commands.getoutput('tmux save-buffer -')

if __name__ == '__main__':

    before = get_now_tmux_buffer()

    while True:

            if before != get_now_tmux_buffer():
                os.system('tmux save-buffer -|xsel --input --clipboard --display :0')
                before = get_now_tmux_buffer()

            time.sleep(1)
