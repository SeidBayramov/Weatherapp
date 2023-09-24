from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'
api_key = '5c4ba25bd9caa31d1149f5c68d5caf4d'


def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country'] 
        temp_kelvin = json['main']['temp']
        temp_celsius = round(temp_kelvin - 273.15, 2) 
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, icon, weather)
        return final
    else:
        return None 
    
def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        temp_lbl['text'] = '{:.2f}ºC'.format(weather[2])
        weather_lbl['text'] = weather[4] 
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

app = Tk()
app.title("Weather app")

app.geometry('400x350')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search weather', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='Location', font=('bold', 20))
location_lbl.pack()

weather_lbl = Label(app, text='Weather')
weather_lbl.pack()

temp_lbl = Label(app, text='Temperature')
temp_lbl.pack()

image = Label(app)
image.pack()

app.mainloop()
