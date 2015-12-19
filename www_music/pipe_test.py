#!/usr/bin/python

import sys
import os
import subprocess
import time

print "hello python!!"
keycon = "keycon.txt"
if os.path.exists(keycon):
   os.system("rm -f %s"%keycon)

# pipe = subprocess.Popen ("mplayer ../video/20130907_car.avi & ", shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
while 1:
   if os.path.exists(keycon):
      fp = open (keycon, "r")
      key_val = fp.readline().replace("\n", "")
      print "/%s/"%key_val
      fp.close
      if key_val == "q":
         exit()
      # pipe.stdin.write("\x1b[C")
      os.system("rm -f %s"%keycon)
# os.system("sleep 3")
