import os
import time
import mysql.connector
import mysql

query = ("SELECT *  FROM tu.agile_central "
                 "WHERE id='US1234'")

print("starting dance party")
time.sleep(2)
print("spinning up lights")
time.sleep(2)
print("Starting fog machine")
time.sleep(2)
print("Ready to party!")
time.sleep(2)



while 1==1:

    cnx = mysql.connector.connect(host='localhost', user='pi', passwd='martyweb', db='tu')
    print('Checking status')
    time.sleep(1)
    cursor = cnx.cursor()

    rows=''
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()    
    
    for x in rows:
         if(x[1] == 'Complete'):
             print('Party!!!!!!!!!!!!!!!!!')
             os.system("aplay DJ\ Airhorn\ Sound\ Effect.wav")
             time.sleep(100)
             break
         else:
             print("Status is " + x[1])
         
         
         
    time.sleep(2)




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

	

