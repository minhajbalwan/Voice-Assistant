from keyboard import press, write
from playsound import playsound
from time import sleep
from gtts import gTTS
import wolframalpha
import Alarm_util
import webbrowser
import wikipedia
import pyautogui
import os

def speak(audio):
	voice = gTTS(audio, slow=False)
	voice.save('features.mp3')
	playsound('features.mp3')
	os.remove('features.mp3')

def Search(term):
	try:
		webbrowser.open('https://en.wikipedia.org/wiki/Main_Page', new=1, autoraise=True)
		sleep(5)
		pyautogui.click(x=1100, y=165)
		sleep(1)
		write(term)
		sleep(2)
		press('enter')
		result = wikipedia.summary(term, 2)
		speak(result)
		pyautogui.hotkey('ctrl', ('w'))
		pass
	except Exception as e:
		speak('Sorry try again later')
		pass

def Wolfram(query):
	app_id = "Y7XLR4-TQKUQEG8W4"
	requester = wolframalpha.Client(app_id)
	requested = requester.query(query)

	try:
		answer = next(requested.results).text
		return answer
	except Exception as e:
		speak('Sorry cant do that')

def Calculator(query):
	term = str(query)

	term = term.replace("multiply by", "*")
	term = term.replace("multiplied by", "*")
	term = term.replace("into", "*")
	term = term.replace("plus", "+")
	term = term.replace("minus", "-")
	term = term.replace("divide", "/")
	term = term.replace("by", "/")

	final = str(term)
	
	try:
		result = Wolfram(final)
		speak(result)
	except Exception as e:
		speak('Sorry, try again later')

def Temp(query):
	try:
		term = str(query)
		term = term.replace('temperature', "")
		term = term.replace('what', "")
		term = term.replace("what's", "")
		term = term.replace('is', "")
		term = term.replace('the', "")
		term = term.replace('in', "")
		tempQuery = str(term)

		if 'outside' in tempQuery:
			area = "Temperature in Jammu"
			result = Wolfram(area)
			speak(result)
		else:
			area = "temperature in" + tempQuery
			result = Wolfram(area)
			speak(f"{area} is {result}")

	except Exception as e:
		speak('Sorry try again later')

def Alarm(query):
	TimeHere = open('Data.txt','a')
	TimeHere.write(query)
	TimeHere.close()
	Alarm_util.run()