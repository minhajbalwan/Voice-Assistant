import Alarm_util

def Alarm(query):
	TimeHere = open('Data.txt','a')
	TimeHere.write(query)
	TimeHere.close()
	Alarm_util.run()

Alarm("set alarm for 10 20 am")