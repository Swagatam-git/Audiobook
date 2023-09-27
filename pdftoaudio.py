import pyttsx3
import PyPDF2

book=open('Computer Networking Notes for Tech Placements.pdf','rb')

'''In Python, files can be opened in two modes: text mode and binary mode. 
Text mode is the default mode, and it is used for reading and writing text files, 
while the binary mode is used for reading and writing binary files.'''

reader=PyPDF2.PdfReader(book)
totalpage=len(reader.pages)
print(totalpage)

speaker=pyttsx3.init()#initialize an instance
voice = speaker.getProperty('voices')#get the available voices
speaker.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice

x=int(input("Enter page no to start : "))

for i in range(x-1,totalpage):
     page=reader.pages[i]
     text=page.extract_text()
     speaker.say(text)
     speaker.runAndWait()

