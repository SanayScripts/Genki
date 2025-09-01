from pathlib import Path
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sanay\Desktop\Genki\main\assets\frame42")

def run_program(program):
    window.destroy()
    subprocess.Popen(["python", program])
                     
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


selected_sex = ""
selected_activity = ""


def male_button_clicked():
    global selected_sex
    selected_sex = "Male"
    print("Sex selected:", selected_sex)


def female_button_clicked():
    global selected_sex
    selected_sex = "Female"
    print("Sex selected:", selected_sex)


def sedentary_button_clicked():
    global selected_activity
    selected_activity = "Sedentary"
    print("Activity level selected:", selected_activity)


def moderate_button_clicked():
    global selected_activity
    selected_activity = "Moderate"
    print("Activity level selected:", selected_activity)


def active_button_clicked():
    global selected_activity
    selected_activity = "Active"
    print("Activity level selected:", selected_activity)


def calculate_and_display():
    age = entry_3.get()
    sex = selected_sex
    weight = entry_1.get()
    height = entry_2.get()

    try:
        if not age or not weight or not height or not sex or not selected_activity:
            raise ValueError("Please fill in all fields.")

        age = int(age)
        weight = float(weight)
        height = float(height)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    if sex not in ["Male", "Female"]:
        messagebox.showerror("Error", "Please select sex.")
        return

    if not (weight > 0 and height > 0 and age > 0):
        messagebox.showerror("Error", "Please enter valid values for age, weight, and height.")
        return

    # Calculate BMR
    if sex == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # Calculate TDEE
    if selected_activity == "Sedentary":
        tdee = bmr * 1.2
    elif selected_activity == "Moderate":
        tdee = bmr * 1.55
    else:  # selected_activity == "Active"
        tdee = bmr * 1.725

    # Calculate weight lost/gained and caloric intake for each category
    weight_change = [2, 1, 0, -1, -2]
    caloric_intake = [tdee + 500, tdee + 250, tdee, tdee - 250, tdee - 500]

    # Clear previous content in table
    for row in tree.get_children():
        tree.delete(row)

    # Insert rows into the Treeview
    for i, (row, weight_change_value, caloric_intake_value) in enumerate(
            zip(["Major Bulk", "Minor Bulk", "Maintenance", "Minor Cut", "Major Cut"], weight_change,
                caloric_intake), start=1):
        tree.insert("", "end", values=[row, weight_change_value, caloric_intake_value])



window = Tk()

window.geometry("1280x720")
window.configure(bg = "#F4F4F4")


canvas = tk.Canvas(
    window,
    bg="#FFFFFF",  # Set background color of canvas
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.1708984375,
    100.0,
    370.1708984375,
    720.0,
    fill="#C3C3C3",
    outline=""
)

button_image_1 = tk.PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = tk.Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=active_button_clicked,
    relief="flat"
)
button_1.place(
    x=53.8291015625,
    y=557.7001953125,
    width=261.25,
    height=47.5
)

button_image_2 = tk.PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = tk.Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=moderate_button_clicked,
    relief="flat"
)
button_2.place(
    x=53.8291015625,
    y=510.2001953125,
    width=261.25,
    height=47.5
)

button_image_3 = tk.PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = tk.Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=sedentary_button_clicked,
    relief="flat"
)
button_3.place(
    x=53.8291015625,
    y=462.7001953125,
    width=261.25,
    height=47.5
)

canvas.create_text(
    55.09588623046875,
    428.5,
    anchor="nw",
    text="Activity",
    fill="#414141",
    font=("SFPro Regular", 19 * -1)
)

entry_image_1 = tk.PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    250.00413513183594,
    381.9501953125,
    image=entry_image_1
)
entry_1 = tk.Entry(
    bd=0,
    bg="#F4F4F4",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=184.92913818359375,
    y=358.2001953125,
    width=130.14999389648438,
    height=45.5
)

button_image_4 = tk.PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = tk.Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=calculate_and_display,
    relief="flat"
)
button_4.place(
    x=53.8291015625,
    y=627.0,
    width=261.0,
    height=50.0
)

entry_image_2 = tk.PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    119.85406494140625,
    381.9501953125,
    image=entry_image_2
)
entry_2 = tk.Entry(
    bd=0,
    bg="#F4F4F4",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=55.72906494140625,
    y=358.2001953125,
    width=128.25,
    height=45.5
)

canvas.create_text(
    188.09588623046875,
    324.0,
    anchor="nw",
    text="Weight (kg)",
    fill="#414141",
    font=("SFPro Regular", 19 * -1)
)

canvas.create_text(
    55.09588623046875,
    324.0,
    anchor="nw",
    text="Height (cm)",
    fill="#414141",
    font=("SFPro Regular", 19 * -1)
)

entry_image_3 = tk.PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    184.7708740234375,
    278.400146484375,
    image=entry_image_3
)
entry_3 = tk.Entry(
    bd=0,
    bg="#F4F4F4",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=54.1458740234375,
    y=254.650146484375,
    width=261.25,
    height=45.5
)

canvas.create_text(
    55.09588623046875,
    221.400146484375,
    anchor="nw",
    text="Age",
    fill="#414141",
    font=("SFPro Regular", 19 * -1)
)

button_image_5 = tk.PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = tk.Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=female_button_clicked,
    relief="flat"
)
button_5.place(
    x=183.97906494140625,
    y=148.25,
    width=131.4168243408203,
    height=47.5
)

button_image_6 = tk.PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = tk.Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=male_button_clicked,
    relief="flat"
)
button_6.place(
    x=54.1458740234375,
    y=148.25,
    width=128.88319396972656,
    height=47.5
)

canvas.create_text(
    54.779052734375,
    115.0,
    anchor="nw",
    text="Sex",
    fill="#414141",
    font=("SFPro Regular", 19 * -1)
)

image_image_1 = tk.PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    824.8291015625,
    409.0,
    image=image_image_1
)

image_image_2 = tk.PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    640.1708984375,
    50.0,
    image=image_image_2
)

image_image_3 = tk.PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    48.8291015625,
    50.0,
    image=image_image_3
)

canvas.tag_bind(image_3, '<Button-1>', lambda event: run_program('C:/Users/Sanay/Desktop/Genki/main/home.py'))


# Create a frame for the table within the bounds of image_1
table_frame = ttk.Frame(window, width=760, height=520)
# Calculate the size of table_frame
table_frame_width = 760
table_frame_height = 520

# Define the center point of image_1
image_1_center_x = 853
image_1_center_y = 360

# Calculate the position of table_frame relative to the center of image_1
table_frame_x = (image_1_center_x - table_frame_width / 2)+50
table_frame_y = image_1_center_y - (table_frame_height -500)
# Place table_frame at the calculated position
table_frame.place(x=table_frame_x, y=table_frame_y)
# Create the table headers
headers = ["", "Weight Lost/Gained per Week", "Caloric Intake"]

# Create the Treeview widget
tree = ttk.Treeview(table_frame, columns=headers, show="headings", height=5)

# Add columns to the Treeview
for col in headers:
    tree.heading(col, text=col)

# Insert rows into the Treeview
rows = ["Major Bulk", "Minor Bulk", "Maintenance", "Minor Cut", "Major Cut"]
for i, row in enumerate(rows, start=1):
    tree.insert("", "end", values=[row, "", ""])

# Place the Treeview widget
tree.grid(row=1, column=0, sticky="nsew")


window.resizable(False, False)
window.mainloop()
