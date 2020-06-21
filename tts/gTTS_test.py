from gtts import gTTS

# English 버전
text ="Good morning. everyone. 식사는 하셨어요?"
tts_en = gTTS(text=text, lang='en')
tts_en.save("gTTSen.mp3")

# Korean 버전
text ="안녕하세요. 여러분. Good bye. How are you today?"
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save("gTTSko.mp3")

"""
f = open("gTTSen.mp3", 'a')
tts_en.write_to_fp(f)
tts_en.write_to_fp(f)
tts_ko.write_to_fp(f)
f.close() """
