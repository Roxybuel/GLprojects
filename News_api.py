import requests
import tkinter as tk

# this creates the window
window = tk.Tk()

# this changes the window title and size
window.title("News Headlines")
window.geometry("400x200")
window.config(bg="#de2d20")

# this creates a label to display the news
news_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#9e2323")
news_label.pack(pady=10)

# this creates a frame to hold the input field and button
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# this creates the input field for the country/city
location_entry = tk.Entry(input_frame, width=30)
location_entry.pack(side=tk.LEFT, padx=5)


# this creates the button to get the news
def get_news():
    # this gets the country/city from the input field
    location = location_entry.get()

    url = "https://newsapi.org/v2/top-headlines?q={0}&apiKey=e1bb7f46f2284cf48516b85dbb6c4f51".format(location)
    response = requests.get(url)
    data = response.json()

    # If the response status is "ok" it will update the LABEL with the top headlines
    if data["status"] == "ok":
        news = ""
        for article in data["articles"]:
            news += f"{article['title']} \n\n"
            news += f"{article['description']} \n\n"
            news += f"{article['url']} \n\n"
            news += "---------------------------- \n\n"

        news_label.config(text=news)

    else:
        news_label.config(text="Error fetching data.")


get_news_button = tk.Button(input_frame, text="Get News", command=get_news)
get_news_button.pack(side=tk.LEFT, padx=5)

# this runs the program
window.mainloop()
