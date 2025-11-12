import tkinter as tk
from PIL import Image, ImageTk
import random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
BLOCK_LENGTHS = [5, 4, 3, 2]
DIRECTIONS = ["right", "left", "right"]
FONT_TITLE = ("Trajan Pro", 18, "bold")
FONT_INPUT = ("Consolas", 14)
FONT_BUTTON = ("Segoe UI", 11, "bold")
FONT_OUTPUT = ("Consolas", 14, "bold")
FONT_INFO = ("Segoe UI", 9)
BG_COLOR = "black"
TEXT_COLOR = "white"
BUTTON_COLOR = "blue"
ERROR_COLOR = "red"
INFO_COLOR = "lightgray"


def generate_key():
    text = entry.get().strip()

    if len(text) != 3:
        output_label.config(
            text="Введите ровно 3 цифры",
            fg=ERROR_COLOR
        )
        return
        
    if not text.isdigit():
        output_label.config(
            text="Допустимы только цифры",
            fg=ERROR_COLOR
        )
        return

    numbers = [int(digit) for digit in text]


    block1 = ''.join(random.choices(ALPHABET, k=5))
    blocks = [block1]
    current = block1

    for i in range(3):
        shift = numbers[i]
        direction = DIRECTIONS[i]
        source = current[1:]
        
        shifted = []
        for char in source:
            idx = ALPHABET.index(char)
            if direction == "right":
                new_idx = (idx + shift) % len(ALPHABET)
            else:
                new_idx = (idx - shift) % len(ALPHABET)
            shifted.append(ALPHABET[new_idx])

        new_block = ''.join(shifted[:BLOCK_LENGTHS[i + 1]])
        blocks.append(new_block)
        current = new_block

    key = f"{blocks[0]}-{blocks[1]}-{blocks[2]}-{blocks[3]}"
    output_label.config(text=key, fg=TEXT_COLOR)


root = tk.Tk()
root.title("Fortnite")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)


bg_image = Image.open("fortnite.jpg")
bg_image = bg_image.resize((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


frame = tk.Frame(root, bg=BG_COLOR)
frame.place(relx=0.5, rely=0.5, anchor="center")


title = tk.Label(
    frame,
    text="Fortnite",
    font=FONT_TITLE,
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
title.pack(pady=(10, 10))


input_label = tk.Label(
    frame,
    text="Введите трёхзначное число (например, 123):",
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
input_label.pack()

entry = tk.Entry(
    frame,
    width=10,
    font=FONT_INPUT,
    justify="center"
)
entry.pack(pady=5)


btn = tk.Button(
    frame,
    text="Сгенерировать ключ",
    font=FONT_BUTTON,
    bg=BUTTON_COLOR,
    fg=TEXT_COLOR,
    activebackground=BUTTON_COLOR,
    command=generate_key
)
btn.pack(pady=8)


output_label = tk.Label(
    frame,
    text="",
    font=FONT_OUTPUT,
    fg=TEXT_COLOR,
    bg=BG_COLOR
)
output_label.pack(pady=8)


info_label = tk.Label(
    frame,
    text="Формат: XXXXX-XXXX-XXX-XX",
    fg=INFO_COLOR,
    bg=BG_COLOR,
    font=FONT_INFO
)
info_label.pack(pady=(4, 10))

root.mainloop()