from playsound import playsound
from gtts import gTTS
import datetime
import os

def speak(audio):
	voice = gTTS(audio, slow=False)
	voice.save('alarm.mp3')
	playsound('alarm.mp3')
	os.remove('alarm.mp3')

def RingerNow(time):
	time_to_set = str(time)
	arr = time_to_set.split()
	time_now = ':'.join(arr[3:5])

	Alarm_time = str(time_now)
	speak(f"Alarm set for {Alarm_time}")
	while True:
		current_time = datetime.datetime.now().strftime("%H:%M")
		if current_time == Alarm_time:
			speak("Wake up")
			break
		elif current_time > Alarm_time:
			break

def run():
	extracted_time = open('Data.txt', 'rt')
	time = extracted_time.read()
	Time = str(time)

	delete_time = open("Data.txt", "r+")
	delete_time.truncate(0)
	delete_time.close

	RingerNow(Time)