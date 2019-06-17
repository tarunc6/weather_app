import tkinter as tk
from tkinter import font
import requests

HEIGHT = 700
WIDTH = 800

def test_function(entry):
	print("hi",entry)

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature(F): %s' % (name, desc, temp)
	except:
		final_str = "There was a problem retreving the data\nPlease try again"
	return final_str
	   

def get_weather(city):
	weather_key = 'ec2e21af57a96c781422fb0e5ffda305'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params ={'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

   


root = tk.Tk()

photo = tk.PhotoImage(file = "landscape.png")
w = tk.Label(root, image=photo)
w.pack()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Modern, 20'))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Modern, 20'), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lowerframe = tk.Frame(root, bg='#80c1ff', bd=10)
lowerframe.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lowerframe, font=('Modern, 20'), anchor = 'nw', justify = 'left', bd = 4)
label.place(relwidth=1, relheight=1)

root.mainloop()