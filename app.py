import tkinter as tk
from tkinter import StringVar
from get_data import name_of_station, nearest_stop_time, line, response, query
from datetime import datetime

import requests
import json

root = tk.Tk()
remaining_time_msg_str_var = StringVar()
root.geometry('640x480')
root.title("Timetables")

def refresh_time():
        response = requests.post('https://api.entur.io/journey-planner/v3/graphql', data=query)
        response = json.loads(response.text)

        nearest_stop_time = response['data']['stopPlace']['estimatedCalls'][0]['aimedArrivalTime']
        # get the current time
        current_time = datetime.now()

        # convert to string so we can edit it
        current_time = str(current_time)
        current_time = current_time.split(" ", 2)[1]
        current_time = current_time.split(".", 1)[0]
        current_time = current_time.rsplit(":", 1)[0]

        shortened_bus_arrival_time = str(nearest_stop_time)
        shortened_bus_arrival_time = shortened_bus_arrival_time.split("T", 1)[1]
        shortened_bus_arrival_time = shortened_bus_arrival_time.split("+", 1)[0]
        shortened_bus_arrival_time = shortened_bus_arrival_time.rsplit(":", 1)[0]
        name_of_line = line['line']['name']
        time_left = int( str(shortened_bus_arrival_time.replace(":", "")) ) - int( str(current_time.replace(":", "")) )
        
        print(shortened_bus_arrival_time)
        if time_left < 0:
                time_left_message = '[{0}]'.format(str(name_of_line)) + '[{0}] '.format(shortened_bus_arrival_time) +" The bus is late by " + str()
        elif time_left == 0:
                time_left_message = '[{0}]'.format(str(name_of_line)) + '[{0}] '.format(shortened_bus_arrival_time) + " The bus is arriving now."
        else:
                time_left_message = '[{0}]'.format(str(name_of_line)) + '[{0}] '.format(shortened_bus_arrival_time) + " ca. " + str(time_left) + " minutes remaining."

        print(nearest_stop_time)
        print("Timetable updated: " + str(time_left_message))

        # update time left message
        remaining_time_msg_str_var.set(time_left_message)

        return remaining_time_msg_str_var

remaining_time_display_msg = refresh_time()

bg_frame = tk.Frame(root, bg="#eeeeee")
bg_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

bg_label = tk.Label(bg_frame, bg="#dddddd")
bg_label.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

station_name_label = tk.Label(bg_frame, bg="#eeffff", text=name_of_station, font=100, fg="#555555")
station_name_label.place(relx= 0.5-0.35, rely=0.4-0.25, relwidth=0.7, relheight=0.25)

display_remaining_time_label = tk.Label(bg_frame, bg="#ffffff", textvariable=remaining_time_display_msg, fg="#555555")
display_remaining_time_label.place(relx=0.5-0.35, rely=0.5, relwidth=0.7, relheight=0.2)

refresh_button = tk.Button(bg_frame, bg="#fefecc", text="Refresh", command=refresh_time)
refresh_button.place(relx=0.25, rely=0.85, relwidth=0.5, relheight=0.1)

root.mainloop()
