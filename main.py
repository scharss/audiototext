//Scharss https://scharss.github.io/

import speech_recognition as sr

r=sr.Recognizer()

a=sr.AudioFile('numw.wav')
with a as source :
	audio=r.record(source)

text=r.recognize_google(audio, language="es-CO")


file1=open(r"C:\Users\user\Documents\CURSOS\PYTHON\EJERCICIOS\adi.txt","a")
file1.writelines(text)
file1.close()
