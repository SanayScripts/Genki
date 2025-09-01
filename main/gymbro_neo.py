from pathlib import Path
from tkinter import Tk, Canvas, Text, Entry, PhotoImage
import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()  # Load environment variables from .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

def submit_question():
    question = entry_2.get().strip()  # Retrieve input from entry_2
    try:
        response = get_gemini_response(question)
        conversation = f"{response}\n\n"
        entry_1.insert("end", conversation)  # Insert response into entry_1
    except Exception as e:
        print("Error occurred:", e)

Assets_PATH = Path(r"C:\Users\Sanay\Documents\Genki Final Draft\build\assets\frame43")

def relative_to_assets(path: str) -> str:
    return str(Assets_PATH / Path(path))

# Initialize Tkinter
window = Tk()
window.geometry("1280x720")
window.title("Genki Gymbro")

canvas = Canvas(
    window,
    bg="#F4F4F4",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Output  entry (entry_1)
entry_1 = Text(
    window,
    bd=0,
    bg="#E8E8E8",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=290.6666564941406,
    y=282.0,
    width=698.6666870117188,
    height=346.0
)

# Input entry (entry_2)
entry_2 = Entry(
    bd=0,
    bg="#E8E8E8",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=291.3330078125,
    y=156.0,
    width=698.6666870117188,
    height=48.66666793823242
)

canvas.create_text(
    290.8291015625,
    253.0,
    anchor="nw",
    text="output",
    fill="#414141",
    font=("SFPro Medium", 16 * -1)
)

canvas.create_text(
    288.8291015625,
    127.0,
    anchor="nw",
    text="Input",
    fill="#414141",
    font=("SFPro Medium", 16 * -1)
)

canvas.create_text(
    57.3330078125,
    56.0,
    anchor="nw",
    text="Genki Gymbro",
    fill="#414141",
    font=("SFPro Medium", 30 * -1)
)

image_image_1 = PhotoImage(file=relative_to_assets('image_1.png'))
image_1 = canvas.create_image(
    1037.103515625,
    182.3701171875,
    image=image_image_1
)
canvas.tag_bind(image_1, "<Button-1>", lambda event: submit_question())  # Fix for lambda event

# Run the Tkinter event loop
window.resizable(False, False)
window.mainloop()
