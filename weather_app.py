import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

PRIMARY_COLOR = "#80808A"
SECONDARY_COLOR = "#1F1FD1"
BACKGROUND_COLOR = "#262666"
TEXT_COLOR = "#80808A"
ENTRY_COLOR = "#FFFFFF"
TITLE_COLOR = "#FFFFFF"

def get_weather(city):
    API_key = "1b2f8c4cbcbd0ee0ce628c4130e28dc2"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None
    
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

def update_weather_display():
    city = city_entry.get()
    result = get_weather(city)
    
    if result:
        icon_url, temperature, description, city, country = result
        location_label.config(text=f"{city}, {country}", fg=TEXT_COLOR)
        
        image = Image.open(requests.get(icon_url, stream=True).raw)
        icon = ImageTk.PhotoImage(image)
        icon_label.config(image=icon)
        icon_label.image = icon
        
        temperature_label.config(text=f"Temperature: {temperature:.2f}°C", fg=TEXT_COLOR)
        description_label.config(text=f"Description: {description}", fg=TEXT_COLOR)
        
        title_label.pack_forget()
        github_label.pack_forget() 

    else:
        github_label.pack()

def on_entry_click(event):
    if city_entry.get() == "Search for City":
        city_entry.delete(0, tk.END)

def on_enter_key(event):
    if event.keysym == "Return":
        update_weather_display()

root = tk.Tk()
root.title("Weather by Jonas")
root.geometry("400x500")
root.configure(bg=BACKGROUND_COLOR)

version_label = tk.Label(root, text="Version 1.1", font=("Helvetica", 10), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
version_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 18), bg=PRIMARY_COLOR, fg="white", borderwidth=2, relief=tk.SUNKEN)
city_entry.pack(pady=5, padx=5, fill=tk.X)
city_entry.insert(0, "Search for City")
city_entry.bind("<FocusIn>", on_entry_click)
city_entry.bind("<Return>", on_enter_key)

search_button = tk.Button(root, text="Search", command=update_weather_display, bg=PRIMARY_COLOR, fg="white", font=("Helvetica", 14))
search_button.pack(pady=10)

location_label = tk.Label(root, font=("Helvetica", 25), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
location_label.pack(pady=20)

icon_label = tk.Label(root, bg=BACKGROUND_COLOR)
icon_label.pack()

temperature_label = tk.Label(root, font=("Helvetica", 20), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
temperature_label.pack()

description_label = tk.Label(root, font=("Helvetica", 20), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
description_label.pack()

made_by_label = tk.Label(root, text="Made by repl1kaDEV", font=("Helvetica", 7), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
made_by_label.pack(side=tk.BOTTOM, pady=10)

title_label = tk.Label(root, text="Weather App", font=("Archivo Black", 25), bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
title_label.pack(pady=10)

github_label = tk.Label(root, text="github.com/repl1kaDEV", font=("Helvetica", 12), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
github_label.pack()

root.mainloop()



###############################
# Made by repl1ka
# github.com/repl1kaDEV
###############################