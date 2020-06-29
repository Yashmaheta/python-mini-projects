from tkinter import*
import os
root=Tk()
root.geometry("700x400")
root.title("youtube Downloader")
def run():
    os.startfile('link.bat')
def download():
    with open('link.bat','w')as down_load:
        down_load.write(f"youtube-dl{link.get()}")
        down_load.close()
    run()

f=Frame(root)
f.grid()
Label(f,text="========youtube video downloader========",font=("arial 15 bold"),fg="red",padx=6).pack(fill=X)
f1=Frame(root)
f1.grid()

Label(f1,text="Enter link Here",font=("arial 15 bold")).grid(row=2)

link=StringVar()

Entry(f1,font=("arial 15"),textvariable=link).grid(row=2,column=1,pady=5,padx=10)
Button(f1,text="Download",padx=50,relief=RAISED,font=10,bd=5,command=download).grid(column=1,pady=5)



root.mainloop()