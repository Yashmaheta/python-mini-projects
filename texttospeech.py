from tkinter import*
from gtts import gTTS
from playsound import playsound

def text():
    text=entery.get()
    speech=gTTS(text=text,lang="en")
    speech.save(r'C:\Users\YASH MAHETA\Pycharm\projects\speech.mp3')
    playsound(r'C:\Users\YASH MAHETA\Pycharm\projects\speech.mp3')




root=Tk()
root.geometry("200x70")
root.title("Text To Speech")


label=Label(root,text="Enter Here:")
label.grid(row=0,column=0)

entery=Entry(root)
entery.grid(row=0,column=1)

button=Button(root,text=("go"),command=text)
button.grid(row=1,column=1)
root.mainloop()