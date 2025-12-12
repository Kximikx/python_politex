import tkinter as tk

window = tk.Tk()
window.title("Завдання 4.2.1")

def change_button():
    button.config(width=30, height=3, text="Гусятин")  

button = tk.Button(window, text="Натисни мене", command=change_button)
button.pack(padx=20, pady=20)

window.mainloop()
