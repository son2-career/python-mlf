import webbrowser
import time
total_breaks = 2 # no. of breaks required
interval = 5 # in seconds
break_count = 0

print ("This program started on " + time.ctime())
while break_count < total_breaks:
	time.sleep(interval)
	webbrowser.open("https://www.youtube.com/watch?v=Y4fodpIwal8")
	print ("Interval no. - " + str(break_count +1) + " at " + time.ctime())
	break_count += 1
