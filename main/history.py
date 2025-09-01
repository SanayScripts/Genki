import webbrowser
import subprocess
from pathlib import Path
from pathlib import Path
import matplotlib.pyplot as plt
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
def run_program(program):
    window.destroy()
    subprocess.Popen(["python", program])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sanay\Desktop\Genki\main\assets\frame41")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#F4F4F4")


canvas = Canvas(
    window,
    bg = "#F4F4F4",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    909.0,
    512.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    373.0,
    512.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    222.0,
    233.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    652.0,
    233.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1058.0,
    234.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    640.0,
    50.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    51.1708984375,
    46.66650390625,
    image=image_image_7
)

# image_image_8 = PhotoImage(
#     file=relative_to_assets("graph.jpg"))
# image_8 = canvas.create_image(
#     373,
#     512,
#     image=image_image_8
# )

canvas.create_text(
    580.0,
    236.0,
    anchor="nw",
    text="8",
    fill="#008B05",
    font=("SFPro Medium", 65 * -1)
)

canvas.create_text(
    984.0,
    233.0,
    anchor="nw",
    text="130",
    fill="#8B0000",
    font=("SFPro Medium", 65 * -1)
)

canvas.create_text(
    158.0,
    237.0,
    anchor="nw",
    text="2",
    fill="#CBB702",
    font=("SFPro Medium", 65 * -1)
)

# Read data from CSV file
data = {}
with open('C:/Users/Sanay/Desktop/Genki/main/res/session_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        exercise_name = row['Exercise Name ']
        reps = int(row['Reps'])
        if exercise_name in data:
            data[exercise_name] += reps
        else:
            data[exercise_name] = reps

# Extract names and values from the data dictionary
names = list(data.keys())
values = list(data.values())

# Create subplots
fig, axs = plt.subplots(figsize=(3.5, 2.25), sharey=True)
fig.autofmt_xdate()
# Plot bar chart
axs.bar(names, values)


# Adjust font size of x-axis labels
axs.tick_params(axis='x', labelsize=5)
canvas = FigureCanvasTkAgg(figure=fig, master=window)
canvas.draw()

fig.patch.set_facecolor('#f4f4f4')
plt.tight_layout()
plt.subplots_adjust(left=0.3, right=0.9, top=0.9, bottom=0.4)
# Resize the canvas according to the figsize and place it at the specified coordinates
canvas.get_tk_widget().place(x=720, y=420, width=fig.get_figwidth()*100, height=fig.get_figheight()*100)


window.resizable(False, False)
window.mainloop()
