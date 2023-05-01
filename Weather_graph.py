import tkinter as tk
import matplotlib.pyplot as plt
import requests

# this creates the window
window = tk.Tk()
# this sets the size of the window
window.geometry("400x200")
# this changes the title of the graph
window.title("Weather Graph")


# this function retrieves the weather data and plots the graph
def plot_graph():
    # to get the users input
    country = country_entry.get()
    api_key = '547e4e1e7c99ee57e3ed55b51a3085a2'

    # this retrieves the weather data from the weather api
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={country}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    # this brings out the temperature and date data from the API response
    dates = []
    temps = []
    for forecast in data['list']:
        date_time = forecast['dt_txt']
        date = date_time.split()[0]
        time = date_time.split()[1]
        if time == '12:00:00':  # to make sure it only retrieves daily temperatures
            dates.append(date)
            temp = forecast['main']['temp']
            temps.append(temp)

    # to plot the graph
    plt.rcParams['axes.facecolor'] = '#cfe2f3'
    plt.plot(dates, temps, color='red', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='red', markersize=12)
    plt.ylim(0, 40)  # Setting y-axis range
    plt.xlabel('Date')
    plt.ylabel('Temperature (C)')
    plt.title(f'Temperature Graph for {country.title()}')
    plt.savefig('weather_graph.png', facecolor='#67aeee')
    plt.show()


# the widgets of the gui
country_label = tk.Label(window, text="Enter the name of the country:")
country_label.pack()

# this displays a cursor where the user can type the country
country_entry = tk.Entry(window)
country_entry.pack()

# this displays a button
plot_button = tk.Button(window, text="Plot Graph", command=plot_graph)
plot_button.pack()

# to run the program
window.mainloop()
