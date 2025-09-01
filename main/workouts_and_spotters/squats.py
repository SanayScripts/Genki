import webbrowser
import subprocess
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def open_url(url):
    webbrowser.open(url)

def run_program(program):
    window.destroy()
    subprocess.Popen(["python", program])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sanay\Desktop\Genki\main\assets\frame21")

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
    1017.0,
    406.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    403.0,
    360.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    640.169921875,
    50.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    48.830078125,
    47.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    403.830078125,
    595.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    866.0,
    609.0,
    image=image_image_6
)

canvas.tag_bind(image_6, '<Button-1>', lambda event: open_url('https://youtu.be/jQr-Zo4m0os?si=u4fMfeq8pP2RtJqm'))
canvas.tag_bind(image_2, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/workouts_and_spotters/spotters/squats_spot.py'))
canvas.tag_bind(image_5, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/workouts_legs.py'))

window.resizable(False, False)
window.mainloop()
