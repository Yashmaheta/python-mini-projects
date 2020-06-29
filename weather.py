from  tkinter import*
import requests
import json

root=Tk()
root.title("Yash's  weather report")
root.geometry("500x500")
api="Your API"
url="http://api.openweathermap.org/data/2.5/weather?"

def weather():
    location=entry.get()
    answer=url + "appid=" + api + "&q=" + location
    response=requests.get(answer)
    res=response.json()
    if res["cod"] != "404":
        x=res["main"]
        temprature= x["temp"]
        presure= x["pressure"]
        humidity= x["humidity"]
        y= res["weather"]
        weather_description =y[0]["description"]
        label=Label(root,text=f"Temperature (in kelvin unit)={temp},\n"
                                f"Atmospheric Presure(in hpa unit)={pre},\n"
                                f"humidity(in persentege)={hum},\n"
                                f"description={weather_description}")
        label1.grid(row=2,column=0)
    else:
        label2=Label(root,text="Enter Correct City")
        label2.grid(row=2,column=0)





label=Label(root,text="Enter your city name:",font="lucida 15 bold")
label.grid(row=0,column=0)

entry=Entry(root,font="lucida 15 bold")
entry.grid(row=0,column=1)

button=Button(root,text="Get Weather",font="lucida 15 bold",command=weather)
button.grid(row=1,column=1,sticky="w")



root.mainloop()