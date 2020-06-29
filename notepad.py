from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog  import  askopenfilename, asksaveasfilename
import  os
if __name__ == '__main__':

    root=Tk()
    root.title("yash notepad")
    root.geometry("700x400")

#Add text area

Textarea=Text(root,font="lucida 13")
file=None
Textarea.pack(fill=BOTH,expand=True)
#=============functions====================#
def newfile():
    global file
    root.title("untitled-Notepad")
    file=None
    Textarea.delete(1.0,END)
def  openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[ ("All Files","*.*"),
                                                             ("text Document","*.*") ])
    if file == " ":
        file=None
    else:
        root.title(os.path.basename(file)+ "-Notepad")
        Textarea.delete(1.0,END)
        f=open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()
def  savefile():
    global file
    if file== None:
        file=asksaveasfilename(initialfile='untitled.txt',defaultextension=".txt",filetypes=[ ("All Files","*.*"),
                                                             ("text Document","*.*") ])
        if file=="":
            file=None
        else:
            #save a new file
            f=open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "-Notepad")
            print("file saved")
    else:
        #save the file
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()


def  quitapp():
    root.destroy()
def  copy():
    Textarea.event_generate(("<<Copy>>"))
def  paste():
    Textarea.event_generate(("<<Paste>>"))
def  cut():
    Textarea.event_generate(("<<Cut>>"))
def  about():
    showinfo("Notepad info","Notepad by yash maheta")


#lets create a menubar

Menubar=Menu(root)
#===============file menu starts===============#
filemenu=Menu(Menubar,tearoff=0)
#to open new file
filemenu.add_command(label="New",command=newfile)

#To open already existing file
filemenu.add_command(label="Open",command=openfile)
#To save the current file
filemenu.add_command(label="Save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quitapp)
Menubar.add_cascade(label="file",menu=filemenu)
#===============file menu ends===============#


#===============edit menu starts===============#
editmenu=Menu(Menubar,tearoff=0)

#to copy file
editmenu.add_command(label="Copy",command=copy)
#to paste file
editmenu.add_command(label="Paste",command=paste)

#to cut fle
editmenu.add_command(label="Cut",command=cut)

Menubar.add_cascade(label="Edit",menu=editmenu)
#===============edit menu ends===============#

#===============help menu starts===============#
helpmenu=Menu(Menubar,tearoff=0)

helpmenu.add_command(label="About Notepad",command=about)
Menubar.add_cascade(label="Help",menu=helpmenu)
#===============help menu ends===============#
root.config(menu=Menubar)

#===========addind scrollbar===========#
scrollbar=Scrollbar(Textarea)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=Textarea.yview)
Textarea.config(yscrollcommand=scrollbar.set)


#scrollbarx=Scrollbar(Textarea)
#scrollbarx.pack(fill=X,side=BOTTOM)
#scrollbarx.config(command=Textarea.xview)
#Textarea.config(xscrollcommand=scrollbarx.set)

root.mainloop()