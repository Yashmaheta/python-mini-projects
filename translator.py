from tkinter import*
from googletrans import Translator


def translation():
    word=ent.get()
    trans=Translator(service_urls=['translate.google.com'])
    trans1=trans.translate(word,dest="gujarati")
    label1=Label(root,text=f"translated:{trans1.text}",fg="grey",font="lucide 15 bold")
    label1.grid(row=6,column=1,sticky="w")

root=Tk()
root.geometry("450x220")
root.title("Translator")
label=Label(root,text="Enter your text here:",font="lucida 15 italic")
label.grid(row=0,column=0)
ent=Entry(root,font="lucida 15 italic")
ent.grid(row=0,column=1)
button=Button(root,text="Translate " ,font="lucida 12 bold",command=translation)
button.grid(row=4,column=1) 

root.mainloop()

