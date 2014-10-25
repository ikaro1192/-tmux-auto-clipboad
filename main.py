#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import commands
import os

stock =commands.getoutput('tmux save-buffer -')

while True:
        insert = commands.getoutput('tmux save-buffer -')
        if stock != insert:
                os.system('clear')
                os.system('tmux save-buffer -|xsel --input --clipboard')
                print insert
                print "========================================="
                stock = insert
                print commands.getoutput('date')

        time.sleep(1)
