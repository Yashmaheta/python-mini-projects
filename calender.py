from tkinter import*
import calendar

root=Tk()
root.geometry("500x250")
root.title("Calender")

def text():
    month_str=month.get()
    year_str=year.get()
    month_int=int(month_str)
    year_int=int(year_str)
    cal=calendar.month(year_int,month_int)
    textf.delete(0.0,END)
    textf.insert(INSERT,cal)




label=Label(root,text="Month:",font="arial 15 bold",fg="blue")
label.grid(row=0,column=0)

month=Spinbox(root,from_=1,to=12,width=5)
month.grid(row=0,column=1)

label1=Label(root,text="Year:",font="arial 15 bold",fg="blue")
label1.grid(row=0,column=3)
year=Spinbox(root,from_=1700,to=2100,width=12)
year.grid(row=0,column=4,padx=8)

button=Button(root,text="Show!!",command=text)
button.grid(row=3,column=3)

textf=Text(root,height=30,width=60,fg="red")
textf.grid(row=4,columnspan=8,sticky="w")




root.mainloop()