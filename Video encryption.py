import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np

def encrypt_decrypt_image(path, key, mode):
    img = Image.open(path)
    arr = np.array(img)
    if mode == "encrypt":
        arr = arr ^ key
        img = Image.fromarray(arr)
        img.save("encrypted.png")
    elif mode == "decrypt":
        arr = arr ^ key
        img = Image.fromarray(arr)
        img.save("decrypted.png")

def browse_file():
    file_path.set(filedialog.askopenfilename())

def run(mode):
    if not file_path.get():
        status_label.config(text="❌ Please select an image file", fg="red")
        return

    k = key.get()
    if not k.isdigit():
        status_label.config(text="❌ Enter a valid numeric key", fg="red")
        return

    try:
        encrypt_decrypt_image(file_path.get(), int(k), mode)
        status_label.config(text=f"{mode.capitalize()}ion Complete ✅", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)} ❌", fg="red")


root = tk.Tk()
root.title("Pixel Encryptor 🔐")

file_path = tk.StringVar()
key = tk.StringVar()

tk.Label(root, text="Image Path").pack()
tk.Entry(root, textvariable=file_path).pack()
status_label = tk.Label(root, text="")
status_label.pack()

tk.Button(root, text="Browse", command=browse_file).pack()

tk.Label(root, text="Encryption Key").pack()
tk.Entry(root, textvariable=key).pack()

tk.Button(root, text="Encrypt", command=lambda: run("encrypt")).pack()
tk.Button(root, text="Decrypt", command=lambda: run("decrypt")).pack()

root.mainloop()
