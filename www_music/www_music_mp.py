#!/usr/bin/python

import sys
import os
import subprocess
import time

print "hello python!!"

# edit at github

print sys.argv[0]
if len(sys.argv) > 1:
	para = sys.argv[1]
	if para == "kill":
		os.system ("ps ax | grep mplayer   | grep -v grep >  ps_list.txt")
		os.system ("ps ax | grep omxplayer | grep -v grep >> ps_list.txt")

		fp = open ("ps_list.txt", "r")
		print ("kill -------------------------")
		for line in fp:
			line = line.replace("\n", "")
			ps = line.split()[0]
			print line
			print "kill %s"%ps
			os.system ("kill %s"%ps)
			
		fp.close()
		print ("kill end -------------------------")
			
	exit()



wmf = "www/data/www_music_message.txt"
keycon = "www/data/keycon.txt"
path = "path"
mode = ""
if os.path.exists(keycon):
	os.system("rm -f %s"%keycon)

num = 0
while(1):
	if os.path.exists(keycon):
		pipe.stdin.write("\x1b[C")
		os.system("rm -f %s"%keycon)
	if os.path.exists(wmf):
		# print ("------------cat----------")
		# os.system("cat %s"%wmf)
		print ("-------------------------")
		fp = open (wmf, "r")
		um = {}
		for line in fp:
			line = line.replace("\n", "")
			print line
			ls = line.split(":")
			if len(ls) > 1:
				um[ls[0]] = ls[1]
		fp.close()
		os.system("rm -f %s"%wmf)

		mode = um["mode"]
		if um["mode"] == "exit":
			os.system ("%s kill"%sys.argv[0])
			# os.system ("ps ax | grep mplayer | awk '{print \"kill \" $1}' | tcsh")
			# os.system ("ps ax | grep omxplayer | awk '{print \"kill \" $1}' | tcsh")
			break
		elif um["mode"] == "stop":
			print "stop"
			os.system ("%s kill"%sys.argv[0])
			# os.system ("ps ax | grep mplayer | awk '{print \"kill \" $1}' | tcsh")
			# os.system ("ps ax | grep omxplayer | awk '{print \"kill \" $1}' | tcsh")
		elif um["mode"] == "dir_play":
			print "dir play"
			cur_path = "www/%s"%um[path]
			os.system ("%s kill"%sys.argv[0])
			# os.system ("ps ax | grep mplayer | awk '{print \"kill \" $1}' | tcsh")
			# os.system ("ps ax | grep omxplayer | awk '{print \"kill \" $1}' | tcsh")
			ls = os.listdir ("www/%s"%um["path"])
			fp = open("play_list.lst", "w")
			for l in ls:
				fp.write ("%s/%s\n"%(cur_path, l))
			fp.close()
			pipe = subprocess.Popen ("mplayer -playlist play_list.lst & ", shell=True, stdin=subprocess.PIPE)
			# play_list = os.listdir("www/%s"%um[path])
			# print play_list
			# play_list_cnt = len(play_list)
			# os.system ("touch www/data/www_music.play_done")
			# num = -1
		elif um["mode"] == "file_play":
			print "file play mode"
			os.system ("%s kill"%sys.argv[0])
			# os.system ("ps ax | grep mplayer | awk '{print \"kill \" $1}' | tcsh")
			# os.system ("ps ax | grep omxplayer | awk '{print \"kill \" $1}' | tcsh")
			print "--------------"
			print um["path"]
			print "--------------"
			if um["path"].endswith("avi") or um["path"].endswith("mp4"):
				# os.system ("/usr/bin/mplayer \"www/%s\"& "%(um["path"]))
				# os.system ("omxplayer \"www/%s\"& "%(um["path"]))
				pipe = subprocess.Popen ("omxplayer \"www/%s\"& "%(um["path"]), shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				# os.system ("mplayer \"www/%s\"& "%(um["path"]))
				print "h1"
				print ("play process is running...")
			else:
				print "h1"
				# os.system ("/usr/bin/mplayer \"www/%s\"& "%(um["path"]))
				# os.system ("omxplayer \"www/%s\"& "%(um["path"]))
				pipe = subprocess.Popen ("mplayer \"www/%s\"& "%(um["path"]), shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
				# os.system ("mplayer \"www/%s\"& "%(um["path"]))
				print "h1"
				print ("play process is running...")

		
	# if mode == "dir_play":
	# 	if os.path.exists("www/data/www_music.play_done"):
	# 		if num < play_list_cnt:
	# 			num = num + 1
	# 		else:
	# 			num = 0
	# 		print play_list[num]

	# 		os.system("rm -f play_mp3.csh")
	# 		play_csh = open ("play_mp3.csh", "w")
	# 		play_csh.write ("#!/usr/bin/tcsh\n")
	# 		play_csh.write ("/usr/bin/mplayer -p -o local \"www/%s/%s\" \n"%(um[path],play_list[num]))
	# 		play_csh.write ("touch www/data/www_music.play_done\n\n")
	# 		play_csh.close()
	# 		os.system("rm -rf www/data/www_music.play_done")
	# 		os.system("chmod 755 play_mp3.csh")
	# 		os.system("./play_mp3.csh &")
	os.system("sleep 1")

