from Features import Search, Temp, Calculator, Alarm
from Whatsapp import WhatsappName, WhatsappMsg
import speech_recognition as sr
from playsound import playsound
from datetime import date
from gtts import gTTS
import datetime
import os

def speak(audio):
	voice = gTTS(audio, slow=False)
	voice.save('main.mp3')
	playsound('main.mp3')
	os.remove('main.mp3')

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening...')
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print('Recognizing...')
		query = r.recognize_google(audio)
		print(f"You said: {query}")
	except:
		return ""
  
	return query.lower()

WAKE = 'hello'
try:
	while True:
		query = takeCommand()
		if query.count(WAKE) > 0:
			speak("Yes")
			query = takeCommand()
			query = query.replace(WAKE, "")

			if "time" in query:
				time = datetime.datetime.now().strftime("%I:%M %p")
				speak(f"The time is {time}")

			elif 'date' in query:
				speak(f"Today is {date.today()}")

			# elif 'what' or 'who' in query:
			# 	Search(query)
			
			elif '' or 'nothing' in query:
				pass
			elif 'temperature' in query:
				Temp(query)
			
			elif 'calculate' in query:
				query = query.replace('calculate', "")
				Calculator(query)
			elif 'message' in query:
				query = query.replace('send', '')
				query = query.replace('message', '')
				query = query.replace('whatsapp', '')
				query = query.replace('to', '')
				query = query.replace(' ', '')
				name = str(query)
				speak(f"Did you mean {name}")
				query = takeCommand()
				if 'yes' in query:
					WhatsappName(name)
					speak('What should I write?')
					message = takeCommand()
					WhatsappMsg(message)
					speak(f"Message sent to {name}")
				else:
					speak("Tell me the name")
					name = takeCommand()
					speak(f"Did you mean {name}")
					query = takeCommand()
					if 'yes' in query:
						WhatsappName(name)
						speak('What should I write?')
						message = takeCommand()
						WhatsappMsg(message)
						speak(f"Message sent to {name}")
					else:
						speak('Sorry, name is not cleared to me')
						pass
				
			elif 'thanks' in query or 'thank you' in query:
				speak('Your welcome')
			elif 'alarm' in query:
				Alarm(query)
				pass
			else:
				speak("I can't do that!")
except Exception as e:
	speak('Error while loading up, check internet connection')
	print(e)