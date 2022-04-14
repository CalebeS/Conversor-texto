from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'pt'
sp = gTTS(text="eu te amo", lang=language, slow=False)
sp.save(audio)
playsound(audio)
