import requests     # to get the http requests
from win10toast import ToastNotifier    # To show toast notification on windows 10
import time     # for delay

# Function to get updates of covid - 19 cases
def update():
    request = requests.get("http://covid19-india-adhikansh.herokuapp.com/summary")      # This will get the data from given link
    data = request.json()   # convert the received data into jason format
    # Format the data according the the data received using API
    text = f'Active Cases : {data["Active cases"]} \nCured : {data["Cured/Discharged/Migrated"]} \nDeaths : {data["Death"]} \nTotal Cases : {data["Total Cases"]}'

    # Create a loop to get the data continuously
    while True:
        toast = ToastNotifier()            # Create an object to get the notification on windows 10
        toast.show_toast("Covid-19 Updater", text, duration=10)     # set the toast heading and duration
        time.sleep(60)      # interval for data update

# call the function - Main Program
update()