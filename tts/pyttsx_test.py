import pyttsx3
engine = pyttsx3.init() # Object 생성

""" RATE 설정 """
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

""" VOLUME 설정 """
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

""" VOICE 설정 """
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
#engine.say('My current speaking rate is ' + str(rate))
engine.say('내 소리의 빠르기는 ' + str(rate))
engine.runAndWait()
engine.stop()

""" Saving Voice to a file """
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Test to Speech 테스트', 'test.mp3')
engine.runAndWait()
