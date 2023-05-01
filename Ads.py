import tkinter as tk
from PIL import Image, ImageTk
import random

# a list of all the images used as ads
image_files = ['Image_1.jpg', 'Image_2.jpg.png', 'Image_3.jpg.png', 'Image_4.jpg', 'Image_5.jpg']


def display_image():
    # chooses a random image for the ad
    random_image = random.choice(image_files)

    # opens the image and resizes it to 500x500
    image = Image.open(random_image)
    image = image.resize((500, 500))

    image.save("random_image.png")

    # creates a Tkinter PhotoImage object
    photo = ImageTk.PhotoImage(image)

    # creates a label to display the image
    label.configure(image=photo)
    label.image = photo


# creates a window and label to display the image
window = tk.Tk()
label = tk.Label(window)
label.pack()


# displays the first image
display_image()

# runs the program
window.mainloop()
