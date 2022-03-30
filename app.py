import tkinter as tk
from tkinter import StringVar
from get_data import name_of_station, nearest_stop_time, line, r, delayed_stop_time
from datetime import datetime

root = tk.Tk()
remaining_time_msg_str_var = StringVar()
root.geometry('640x480')
root.title("Timetables")

def refresh_time():
	from get_data import name_of_station, nearest_stop_time, line, r
	nearest_stop_time = r['data']['stopPlace']['estimatedCalls'][0]['aimedArrivalTime']
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

	shortened_bus_arrival_delayed = str(delayed_stop_time)
	shortened_bus_arrival_delayed = shortened_bus_arrival_delayed.split("T", 1)[1]
	shortened_bus_arrival_delayed = shortened_bus_arrival_delayed.split("+", 1)[0]
	shortened_bus_arrival_delayed = shortened_bus_arrival_delayed.rsplit(":", 1)[0]
	name_of_line = line['line']['name']
	time_left = int( str(shortened_bus_arrival_time.replace(":", "")) ) - int( str(current_time.replace(":", "")) )

	if time_left < 0:
		time_left_message = '[{0}]'.format(str(name_of_line)) + " The bus is late."
	elif time_left == 0:
		time_left_message = '[{0}]'.format(str(name_of_line)) + " The bus is arriving now."
	else:
		time_left_message = '[{0}]'.format(str(name_of_line)) + " ca. " + str(time_left) + " minutes remaining."

	print(nearest_stop_time)
	print("Timetable updated: " + str(time_left_message))
	print("Delayed time: " + str(shortened_bus_arrival_delayed))

	# update time left message
	remaining_time_msg_str_var.set(time_left_message)

	return remaining_time_msg_str_var

remaining_time_display_msg = refresh_time()

bg_frame = tk.Frame(root, bg="#ffeeee")
bg_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

station_name_label = tk.Label(bg_frame, bg="#ffffff", text=name_of_station, font=100)
station_name_label.place(relx= 0.5-0.35, rely=0.4-0.25, relwidth=0.7, relheight=0.25)

display_remaining_time_label = tk.Label(bg_frame, bg="#ffffff", textvariable=remaining_time_display_msg)
display_remaining_time_label.place(relx=0.5-0.35, rely=0.5, relwidth=0.7, relheight=0.2)

refresh_button = tk.Button(bg_frame, bg="#fefecc", text="Refresh", command=refresh_time)
refresh_button.place(relx=0.25, rely=0.85, relwidth=0.4, relheight=0.1)

root.mainloop()
