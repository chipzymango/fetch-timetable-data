import tkinter as tk
from win32api import GetSystemMetrics

from get_data import name_of_station, nearest_stop_time, line
from datetime import datetime

# get the current time
current_time = datetime.now()

# convert to string so we can edit it
current_time = str(current_time)
current_time = current_time.split(" ", 2)[1]
current_time = current_time.split(".", 1)[0]
current_time = current_time.rsplit(":", 1)[0]


# get bus arrival time
shortened_bus_arrival_time = str(nearest_stop_time)
shortened_bus_arrival_time = shortened_bus_arrival_time.split("T", 1)[1]
shortened_bus_arrival_time = shortened_bus_arrival_time.split("+", 1)[0]
shortened_bus_arrival_time = shortened_bus_arrival_time.rsplit(":", 1)[0]
print(shortened_bus_arrival_time)

print(current_time)

name_of_line = line['line']['name']

# get the time differance in minutes
time_left = int( str(shortened_bus_arrival_time.replace(":", "")) ) - int( str(current_time.replace(":", "")) )

time_left_message = str(time_left) + " minutes remaining " + "("+shortened_bus_arrival_time+") " + "till " + str(name_of_line)#['id']['name']


root = tk.Tk()

root.geometry('640x480')
root.title("Timetables")

bg_frame = tk.Frame(root, bg="#ffeeee")
bg_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

label1 = tk.Label(bg_frame, bg="#ffffff", text=name_of_station, font=25)
label1.place(relx= 0.5-0.35, rely=0.4-0.25, relwidth=0.7, relheight=0.25)

label2 = tk.Label(bg_frame, bg="#ffffff", text=time_left_message)#,# font=10)
label2.place(relx=0.5-0.35, rely=0.7, relwidth=0.7, relheight=0.2)

root.mainloop()