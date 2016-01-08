#!/usr/bin/python

import time
import subprocess
import os


print ("===========================================")
print ("EBS Recording script...")
print ("===========================================")

Pocket_Chinese = {
	"name" : "Pocket_Chinese",
	"time" : 10
}

Easy_English = {
	"name" : "Easy_English",
	"time" : 19
}

Power_English = {
	"name" : "Power_English",
	"time" : 19
}
c_time = int (time.strftime ("%H%M"))
e_time = 1805
p_time = 1808

pgm_she = {
	500 : Pocket_Chinese,
	720 : Easy_English,
	740 : Power_English
}

# ps = subprocess.Popen ( "mplayer ftp/20150702_072021.wma &" , shell=True)


while (1):
	c_date = int (time.strftime ("%y%m%d"))
	c_time = int (time.strftime ("%H%M"))
	# print ("Date : %s %s"%(c_date, c_time))
	
	cp = 0
	for st in pgm_she.keys():
		st_int = int(st)
		if c_time >= st_int and c_time < st_int+1:
			cp = st_int
			break
	if cp > 0:
		pgm_name = pgm_she[cp]["name"]
		pgm_time = pgm_she[cp]["time"] * 60
		print ("	Recording start... %s (%s)"%(pgm_name, pgm_time))
		file_name = "%s_%s_%s"%(pgm_name, c_date, c_time)
		wma_name = "ebs_wma/%s.wma"%file_name
		mp3_name = "www/pi_disk/ebs/%s.mp3"%file_name
		ps = subprocess.Popen ("rtmpdump -r rtmp://ebsandroid.ebs.co.kr:1935/fmradiofamilypc/familypc1m -B %s -o %s"%(pgm_time, wma_name) , shell=True)
		time.sleep(pgm_time)
		ps.kill()
		os.system ("ffmpeg -i %s -acodec libmp3lame %s &"%(wma_name, mp3_name))
		

	time.sleep (10)

# ps.kill()

# rtmpdump -r rtmp://ebsandroid.ebs.co.kr:1935/fmradiofamilypc/familypc1m -o $file_name.wma &
# set psid = `ps -aux | grep rtmpdump | grep -v grep | awk '{print $2}'`
