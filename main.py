#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import commands
import os

counter = 0
stock =commands.getoutput('parcellite -c')

while counter ==0:
        insert = commands.getoutput('parcellite -c')
        if stock != insert:
                os.system('clear')
                print insert
                print "========================================="
                stock = insert
                print commands.getoutput('date')

        time.sleep(1)
