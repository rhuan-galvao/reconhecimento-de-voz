import speech_recognition as sr
import webbrowser

r = sr.Recognizer()
with sr.Microphone() as source:
    print('Diga algo!')
    audio = r.listen(source)
    
try:
  say = r.recognize_google(audio, language='pt-br')
except sr.UnknownValueError:
    print('Não entendi ;(')
except sr.RequestError as e:
    print(f'Erro ao conectar ao google, {e}')
else:
    say = say.split()
    if say[0] == 'pesquisar':
        del say[0]
        pesquisar = ''
        for palavras in say:
            pesquisar += palavras + ' '
        url = f'https://www.google.com/search?q={pesquisar}&oq=&aqs=chrome..69i57j0l7.831j0j4&sourceid=chrome&ie=UTF-8'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
