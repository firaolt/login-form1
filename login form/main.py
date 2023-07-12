import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.geometry("700x500")
window.iconbitmap(r'world-app.ico')
window.configure(bg="#FFFF00")
window.title("login form to firaol.")

def login():
    username = "firaol tamiru"
    password = "40726897"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login success", message="My name is firaol tamiru.You successfully logged in")
    else:
       messagebox.showerror(title="Error", message="My name is firaol tamiru.Invalid login")

frame = tkinter.Frame(bg="#FFFF00")


login_lable = tkinter.Label(frame, text="login to firaol", bg="#FFFF00", fg="black", font=("Arial", 30))
username_lable = tkinter.Label(frame, text="username", bg="#FFFF00", fg="black", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 15))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 15))
password_lable = tkinter.Label(frame, text="password", bg="#FFFF00" ,fg="black", font=("Arial", 16))
login_button = tkinter.Button(frame, text="login", bg="#FFFF00" ,fg="black", font=("Arial", 15 ), command=login)


login_lable.grid(row=0, column=0, columnspan=2, sticky="nesw", pady=40)
username_lable.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_lable.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)

login_button.grid(row=3, column=0, columnspan=2, pady=30,)

frame.pack()

window.mainloop()
