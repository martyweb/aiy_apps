import os
import time

query = "select u1.user_story_id,"

print("starting dance party")
time.sleep(2)
print("spinning up lights")
time.sleep(2)
print("Starting fog machine")
time.sleep(2)
print("Ready to party!")
time.sleep(2)


while 1=1:

	#JDBC query
	#
#select u1.user_story_id, u1.user_story_status, u2.user_story_id, u2.user_story_status
#from user_story u1
#inner join user_story u2 on u1.user_story_id = u2.user_story_id
#and u1.load_date = CURRENT_DATE()
#and u2.load_date = date_sub(CURRENT_DATE(), 1)
#and u1.user_story_status = 'Accepted'
#and u2.user_story_status != 'Accepted'
#limit 10

	print("Are people here yet?")
	os.system("aplay /home/pi/Downloads/DJ\ Airhorn\ Sound\ Effect.wav")
	sleep(5)

