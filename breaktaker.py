import datetime


def reminder_to_take_a_break():

 total_breaks = 3
 break_count = 0

 print("Please take a break and enjoy this playlist")
 currentDT = datetime.datetime.now()
 print (str(currentDT))

 while (break_count < total_breaks):
     time.sleep(10)
     webbrowser.open("https://youtu.be/YhdX0QuuJUQ")
     break_count = break_count + 1
     break

reminder_to_take_a_break()
