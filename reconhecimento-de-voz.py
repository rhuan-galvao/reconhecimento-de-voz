import speech_recognition
import webbrowser
from urllib.parse import quota

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as microphone:
    print("Diga algo!")
    audio = recognizer.listen(microphone)

try:
  say = recognizer.recognize_google(audio, language="pt-br")
except speech_recognition.UnknownValueError:
    print("Não entendi o que você falou!")
except speech_recognition.RequestError as error:
    print("Erro ao conectar ao google.", error, sep='\n')
else:
    say = say.split()
    
    if say.pop(0) == 'pesquisar':
        pesquisar = ' '.join(say)
        pesquisar = quota(pesquisar)

        url = f'https://www.google.com/search?q={pesquisar}&oq=&aqs=chrome..69i57j0l7.831j0j4&sourceid=chrome&ie=UTF-8'

        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
