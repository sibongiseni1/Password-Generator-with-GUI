import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be at least 8.")
        return

    char_sets = []
    password_chars = []

    if upper_var.get():
        char_sets.append(string.ascii_uppercase)
        password_chars.append(random.choice(string.ascii_uppercase))

    if lower_var.get():
        char_sets.append(string.ascii_lowercase)
        password_chars.append(random.choice(string.ascii_lowercase))

    if digit_var.get():
        char_sets.append(string.digits)
        password_chars.append(random.choice(string.digits))

    if special_var.get():
        special = "!@#$%^&*()_+[]{}|;:,.<>?"
        char_sets.append(special)
        password_chars.append(random.choice(special))

    if not char_sets:
        messagebox.showerror("Selection Error", "Select at least one character type.")
        return

    remaining = length - len(password_chars)
    all_chars = "".join(char_sets)

    password_chars.extend(random.choice(all_chars) for _ in range(remaining))
    random.shuffle(password_chars)

    password = "".join(password_chars)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Password Length (min 8):").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=digit_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=15)

tk.Label(root, text="Generated Password:").pack()
result_entry = tk.Entry(root, width=30)
result_entry.pack()

root.mainloop()