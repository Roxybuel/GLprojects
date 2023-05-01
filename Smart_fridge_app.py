import tkinter as tk
from PIL import Image, ImageTk
from Weather_graph import plot_graph
from News_api import get_news
from Ads import display_image

# this creates the window
window = tk.Tk()
window.geometry("1920x1080")
window.title("Smart Fridge App")

# this loads the weather graph and puts it in the top left part of the window
image = Image.open("weather_graph.png")
image = image.resize((650, 400))
photo = ImageTk.PhotoImage(image)  # this creates a TKINTER PHOTO IMAGE OBJECT with the resized image
label = tk.Label(window, image=photo)  # this creates a label to display the image
label.place(x=0, y=0)  # this sets the position of the label

# this loads the background picture for the news and puts it in the bottom part of the window
user_image = Image.open("Breaking_news2.png")
user_image = user_image.resize((1920, 680))
user_photo = ImageTk.PhotoImage(user_image)
user_label = tk.Label(window, image=user_photo)
user_label.place(x=0, y=400)

# this loads the ads and puts it at the top right part of the window
ad_image = Image.open("random_image.png")
ad_image = ad_image.resize((650, 400))
ad_photo = ImageTk.PhotoImage(ad_image)
ad_label = tk.Label(window, image=ad_photo)
ad_label.place(x=650, y=0)

window.mainloop()
