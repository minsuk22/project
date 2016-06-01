#!/usr/bin/python

import sys
import os
import subprocess
from subprocess import Popen, PIPE
from time import sleep
# update to github

#testing...
#editing at clone
key_up      = "\x1b[A"
key_down    = "\x1b[B"
key_left    = "\x1b[D"
# key_right   = "\027[C"
# key_right   = "\&#x2192;"
key_right =  "\x1b[C"

print ("hello python!!")
keycon = "keycon.txt"
if os.path.exists(keycon):
   os.system("rm -f %s"%keycon)

# pipe = subprocess.Popen ("mplayer 20130907_car.avi", shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
pipe = Popen (['mplayer','hh.mp4'], stdin=PIPE)
# pipe = Popen ('mplayer hh.mp4', stdin=PIPE)
print ("play\n\n")
while 1:
   if os.path.exists(keycon):
      fp = open (keycon, "r")
      key_val = fp.readline().replace("\n", "")
      print ("/%s/"%key_val)
      fp.close()
      if key_val == "q":
         os.system("www_music_mp.py kill")
         exit()
      if key_val == "rew_10":
         pipe.stdin.write(key_left)
      if key_val == "rew_60":
         pipe.stdin.write(key_left)
         pipe.stdin.write(key_left)
         pipe.stdin.write(key_left)
         pipe.stdin.write(key_left)
         pipe.stdin.write(key_left)
         pipe.stdin.write(key_left)
      if key_val == "ff_10":
         pipe.stdin.write(key_right)
      if key_val == "ff_60":
         pipe.stdin.write(key_right)
         pipe.stdin.write(key_right)
         pipe.stdin.write(key_right)
         pipe.stdin.write(key_right)
         pipe.stdin.write(key_right)
         pipe.stdin.write(key_right)
      if key_val == "vol_up":
         pipe.stdin.write("*")
      if key_val == "vol_upup":
         pipe.stdin.write("*")
         pipe.stdin.write("*")
         pipe.stdin.write("*")
         pipe.stdin.write("*")
         pipe.stdin.write("*")
      if key_val == "vol_down":
         pipe.stdin.write("/")
      if key_val == "vol_downdown":
         pipe.stdin.write("/")
         pipe.stdin.write("/")
         pipe.stdin.write("/")
         pipe.stdin.write("/")
         pipe.stdin.write("/")
      os.system("rm -f %s"%keycon)
   # pipe.stdin.write('p')
   sleep(0.5)
   # print ("sleep\n\n")
# os.system("sleep 3")
