import requests
import json
import tkinter as tk


def get_weather(city):
    if city:
        try:
            api_key = '&APPID=3c187e6812c3332a48b4a45c2e6b270d&units=metric'
            url = 'https://api.openweathermap.org/data/2.5/weather?q='
            api_call = url + city + api_key
            api_result = requests.get(api_call)
            load = api_result.content
            j_load = json.loads(load)
            weather = j_load["weather"][0]["main"]
            temp = j_load["main"]["temp"]
            temp_feels_like = j_load["main"]["feels_like"]
            wind = j_load["wind"]["speed"]
            icon = j_load["weather"][0]["icon"]
            Label_city["text"] = "Město: " + entry_city.get()
            Label_temp["text"] = "Aktuální teplota: " + str(temp) + " °C"
            Label_temp_feels_like["text"] = "Pocitová teplota: " + str(temp_feels_like) + " °C"
            Label_weather["text"] = "Počasí: " + str(weather)
            Label_wind["text"] = "Rychlost větru: " + str(wind) + "m/s"
            icon_path = "C:\\Python\\Weather_app\\icons\\{}@2x.png".format(icon)
            icon_image = tk.PhotoImage(file=icon_path)
            Label_icon.configure(image=icon_image, bg="#3abeff")
            Label_icon.image = icon_image
        except KeyError:
            Label_city["text"] = "Město nenalezeno"


root = tk.Tk()
window = root.geometry("700x500")
resize = root.resizable(False, False)
title = root.title("Weather app")
background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame_input = tk.Frame(root, bg='#3abeff')
frame_input.place(relx=0.15, rely=0.1, relheight=0.1, relwidth=0.7)  # 490x50

entry_city = tk.Entry(frame_input, font=35)
entry_city.place(x=5, y=5, relheight=0.8, relwidth=0.765)

but_confirm = tk.Button(frame_input, text="Potvrdit", command=lambda: get_weather(entry_city.get()))
but_confirm.place(relx=0.79, rely=0.125, relheight=0.8, relwidth=0.2)  # 98x40

frame_output = tk.Frame(root, bg='#3abeff')
frame_output.place(x=105, y=150, relwidth=0.7, relheight=0.6)  # 300x490

frame_output_inner = tk.Frame(frame_output, bg="white")
frame_output_inner.place(x=5, y=5, relheight=0.965, relwidth=0.98)  # 294x472,85

Label_city = tk.Label(frame_output_inner, bg="white", font=15, anchor="sw")
Label_city.place(x=5, y=52, relheight=0.1, relwidth=0.4)

Label_weather = tk.Label(frame_output_inner, bg="white", anchor="sw")
Label_weather.place(x=5, y=90, relheight=0.1, relwidth=0.4)

Label_temp = tk.Label(frame_output_inner, bg="white", anchor="sw")
Label_temp.place(x=5, y=128, relheight=0.1, relwidth=0.4)

Label_temp_feels_like = tk.Label(frame_output_inner, bg="white", anchor="sw")
Label_temp_feels_like.place(x=5, y=166, relheight=0.1, relwidth=0.4)

Label_wind = tk.Label(frame_output_inner, bg="white", anchor="sw")
Label_wind.place(x=5, y=204, relheight=0.1, relwidth=0.4)

Label_icon = tk.Label(frame_output_inner, bg="white")
Label_icon.place(x=250, y=52, relwidth=0.3, relheight=0.4)
root.mainloop()
