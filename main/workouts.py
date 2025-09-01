
import webbrowser
import subprocess
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


def run_program(program):
    window.destroy()
    subprocess.Popen(["python", program])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sanay\Desktop\Genki\main\assets\frame40")


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
    947.0,
    212.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    947.0,
    393.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    947.0,
    574.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    336.0,
    212.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    336.0,
    393.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    334.0,
    574.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    640.1708984375,
    50.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    51.0,
    46.66650390625,
    image=image_image_8
)
canvas.tag_bind(image_1, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/workouts_chest.py'))
canvas.tag_bind(image_2, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/workouts_core.py'))
canvas.tag_bind(image_3, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/workouts_cardio.py'))
canvas.tag_bind(image_4, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/workouts_arms.py'))
canvas.tag_bind(image_5, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/workouts_legs.py'))
canvas.tag_bind(image_6, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/workouts_back.py'))
canvas.tag_bind(image_8, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/home.py'))



window.resizable(False, False)
window.mainloop()
