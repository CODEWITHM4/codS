import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length must be at least 4.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        output_entry.config(state='normal')
        output_entry.delete(0, tk.END)
        output_entry.insert(0, password)
        output_entry.config(state='readonly')

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("420x250")
root.resizable(False, False)
root.configure(bg="#222831")

title_label = tk.Label(root, text="Random Password Generator",
                       font=("Helvetica", 16, "bold"), bg="#222831", fg="#FFD369")
title_label.pack(pady=10)

length_label = tk.Label(root, text="Enter Password Length:",
                        font=("Arial", 12), bg="#222831", fg="#EEEEEE")
length_label.pack()

length_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=10)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"),
                            bg="#FFD369", fg="#222831", activebackground="#FFD369",
                            command=generate_password)
generate_button.pack(pady=10)

output_entry = tk.Entry(root, font=("Arial", 14), justify="center", width=30, state='readonly')
output_entry.pack(pady=10)

root.mainloop()
