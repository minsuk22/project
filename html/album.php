<html>
<head>
<title>예준이 동영상!!!</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="user-scalable=no">
<style type='text/css'>
A:link    {color:white; text-decoration:none;}
A:visited {color:red; text-decoration:none; }
A:active  {color:blue; text-decoration:none; }
A:hover   {color:blue; text-decoration:none; }
</style>
</head>
<body bgcolor="black" text="white" width=400>
<font size=7>
<?
	$num = $_GET["num"];
	$dir = $_GET["dir"];
	$mode = $_GET["mode"];
	$target = $_GET["target"];
	if ($mode == "") {
		$mode = "cd";
	}
	if ($dir == "") {
		$dir = "../pi_disk/Yejun";
	}
	$files = scandir("$dir/");
	$n = 1;

	foreach ($files as $f) {
		if(($f == '.') || ($f == '..') || ($f == 'www_music')) { 
			continue;
		}
		if ($num == $n) {
			// echo ("$mode  $dir $target is playing now...<br>\n");
		}
		$n = $n + 1;
	}

	if ($mode != "cd") {
		$fd = fopen("data/www_music_message.txt", 'a+');
		if ($mode == "exit" || $mode == "stop") {
			fwrite ($fd, "mode:$mode\n");
			$play_line = "<center><font size=7 color=#aaaaaa>$mode</font></center>";
		} else {
			if ($mode == "play_dir") {
				fwrite ($fd, "mode:dir_play\n");
				fwrite ($fd, "path:$dir/$target\n");
				$play_line = "$target <font color=#aaaaaa>album is playing...</font>";
			} else if ($mode == "file_play") {
				$target_file = str_replace("_____and_____", "&", $target);
				fwrite ($fd, "mode:file_play\n");
				fwrite ($fd, "path:$dir/$target_file\n");
				$play_line = "$target_file <font color=#aaaaaa> is playing...</font>";
			}
		}
		fwrite ($fd, "\n");
		fclose($fd);
	}

	echo ("<table border=0 cellspacing=0>");
	echo ("<tr><td colspan=2><image src=../pi_disk/album.jpg width=950></td></tr>\n");
	echo ("<tr><td width=700 height=10></td><td width=220></td></tr>\n");
	echo ("<tr><td colspan=2 bgcolor=#222222><center><font size=8>예준이 동영상!!!</font></center></td></tr>\n");
	echo ("<tr><td width=700 height=40></td><td width=220></td></tr>\n");
	echo ("<tr bgcolor=#333333><td colspan=2 width=700><font size=7><b>list : </b></font></td></tr>\n");
	echo ("<tr><td width=700 height=20></td><td width=220></td></tr>\n");

	$n = 1;
	foreach ($files as $f) {
		if(($f == '.') || ($f == '..') || ($f == 'www_music')) { 
			continue;
		}
		if (is_dir("$dir/$f")) {
			echo ("<tr><td width=700 hight=15><a href='index.php?mode=cd&num=$n&dir=$dir/$f&target=$f'             ><font size=7>$f</font></a></td>");
			echo ("<td align=right  ><a href='index.php?mode=play_dir&num=$n&dir=$dir&target=$f'><font size=7>전체 재생</font></a></td></tr>\n");
		} else {
			$target_file = str_replace("&", "_____and_____", $f);
			echo ("<tr><td width=700 colspan=2><a href='$dir/$target_file'><font size=7>$f</font></a></td></tr>\n");
			// echo ("<td align=right  ></td></tr>\n");
		}
		$n = $n + 1;
	}
	echo ("</table>");
	

?>
</font>

</body>
</html>
