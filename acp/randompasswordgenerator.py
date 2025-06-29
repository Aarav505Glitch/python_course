import tkinter as tk
import random
import string
def generate():
    length=int(length_entry.get())
    chars=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(chars) for _ in range(length))
    result_label.config(text=password)
root=tk.Tk()
root.title("password generator")
root.geometry("300x150")
tk.Label(root,text="enter length ").pack()
length_entry=tk.Entry(root)
length_entry.pack()
tk.Button(root,text="generate",command=generate).pack(pady=5)
result_label=tk.Label(root,text="",fg="blue")
result_label.pack()
root.mainloop()



