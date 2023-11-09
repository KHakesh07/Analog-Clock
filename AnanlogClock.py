import tkinter as tk
import math
import time

# Function to update the clock hands
def update_clock():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour % 12  # Convert to 12-hour format

    second_angle = -6 * seconds  # 360 degrees in 60 seconds
    minute_angle = -6 * minutes - 0.1 * seconds  # 360 degrees in 60 minutes
    hour_angle = -30 * hours - 0.5 * minutes  # 360 degrees in 12 hours

    update_hand(second_hand, second_angle)
    update_hand(minute_hand, minute_angle)
    update_hand(hour_hand, hour_angle)

    root.after(1000, update_clock)  # Schedule the update every 1000 milliseconds (1 second)

def update_hand(hand, angle):
    x, y = hand_coords(angle)
    canvas.coords(hand, 150, 150, x, y)

def hand_coords(angle):
    x = 150 + 70 * math.sin(math.radians(angle))
    y = 150 - 70 * math.cos(math.radians(angle))
    return x, y

root = tk.Tk()
root.title("Analog Clock")

# Create a canvas with a circular background
canvas = tk.Canvas(root, width=300, height=300, bg="black")
canvas.pack()

# Create a circular clock face with dots for numbers
canvas.create_oval(50, 50, 250, 250, outline="white", width=2)

# Define the radius for the dots
dot_radius = 5

# Create the dots for the numbers in a circular arrangement
num_dots = 12
for i in range(num_dots):
    angle = math.radians(i * (360 / num_dots))
    x = 150 + 80 * math.cos(angle)
    y = 150 + 80 * math.sin(angle)
    canvas.create_oval(x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius, fill="white")
second_hand = canvas.create_line(150, 150, 150, 50, width=1, fill="red")
minute_hand = canvas.create_line(150, 150, 150, 70, width=3, fill="blue")
hour_hand = canvas.create_line(150, 150, 150, 90, width=4, fill="green")

update_clock()

root.mainloop()
