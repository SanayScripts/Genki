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
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sanay\Desktop\Genki\main\assets\frame44")

  
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

    
window = Tk()

window.geometry("1280x720")
window.configure(bg = "#F4F5F7")


canvas = Canvas(
    window,
    bg = "#F4F5F7",
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
    320.0,
    360.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1170.0,
    57.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    947.0,
    59.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1066.8291015625,
    58.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    807.0,
    498.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    806.8291015625,
    273.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    1115.0,
    273.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    1115.0,
    500.0,
    image=image_image_8
)
canvas.tag_bind(image_2, '<Button-1>', lambda event: open_url('http://www.python.org'))
canvas.tag_bind(image_3, '<Button-1>', lambda event: open_url('http://www.example.com'))
canvas.tag_bind(image_4, '<Button-1>', lambda event: open_url('http://www.anotherexample.com'))

canvas.tag_bind(image_5, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Documents/Disp FY Proj/build/gymbro_neo.py'))
canvas.tag_bind(image_6, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/workouts.py'))
canvas.tag_bind(image_7, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/dietician_42.py'))
canvas.tag_bind(image_8, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/history.py'))

window.resizable(False, False)
window.mainloop()
