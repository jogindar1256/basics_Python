import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 115)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("Good to see you")
engine.runAndWait()
engine.save_to_file('Hello World', 'test.mp3')
engine.stop()
