from tkinter import *
from tkinter import messagebox
import random
import json

# -------------------------------- SEARCH JSON ---------------------------------- #
def search_json():
    site = website_t.get()
    try:
        with open("C:/Users/Olivera/Documents/Python learning/Day30-PasswordManagerUpdate/data.json", "r") as data:
            dataopen = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="No matching values", message="There is no password for this input")
    else:
        if site in dataopen:
            username = dataopen[site]["email"]
            passget = dataopen[site]["password"]
            messagebox.showinfo(title=f"{site}", message=f"Email/Username: {username}\nPassword: {passget}")
        else:
            messagebox.showinfo(title="No matching values", message="There is no password for this input")
        
# --------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = random.randint(8, 10)
    symbols = random.randint(2, 4)
    numbers = random.randint(2, 4)

    passwordgen = []
    for i in range(0, letters):
        passwordgen += chr(random.randint(65, 90))
    for i in range(0, symbols):
        passwordgen += chr(random.randint(33, 47))
    for i in range(0, numbers):
        passwordgen += str(random.randint(0, 9))

    random.shuffle(passwordgen)
    passwo = "".join(passwordgen)
    password_t.insert(0, passwo)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    site = website_t.get()
    username = email_t.get()
    passw = password_t.get()

    new_data = {
        site: {
            "email": username,
            "password": passw
        }
    }

    if len(site) == 0 or len(username) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Oops", message="Some fields are left empty!")
    else:
        try:
            with open("C:/Users/Olivera/Documents/Python learning/Day30-PasswordManagerUpdate/data.json", "r") as data:
                data1 = json.load(data)
        except FileNotFoundError:
            with open("C:/Users/Olivera/Documents/Python learning/Day30-PasswordManagerUpdate/data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            data1.update(new_data)
            with open("C:/Users/Olivera/Documents/Python learning/Day30-PasswordManagerUpdate/data.json", "w") as data:
                json.dump(data1, data, indent=4)
        finally:
            website_t.delete(0, END)
            email_t.delete(0, END)
            password_t.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image = PhotoImage(file="C:/Users/Olivera/Documents/Python learning/Day30-PasswordManagerUpdate/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=1, column=2)

website = Label(text="Website:", font=("Ariel", 10, "normal"))
website.grid(row=2, column=1, sticky="EW")

email = Label(text="Email/Username:", font=("Ariel", 10, "normal"))
email.grid(row=3, column=1, sticky="EW")

password = Label(text="Password:", font=("Ariel", 10, "normal"))
password.grid(row=4, column=1, sticky="EW")

website_t = Entry(width=22)
website_t.grid(row=2, column=2, sticky="EW")
website_t.focus()

search = Button(text="Search", command=search_json, width=14)
search.grid(row=2, column=3, sticky="EW")

email_t = Entry(width=40)
email_t.grid(row=3, column=2, columnspan=2, sticky="EW")

password_t = Entry(width=22)
password_t.grid(row=4, column=2, sticky="EW")

generate_password = Button(text="Generate password", command=generate_pass, width=14)
generate_password.grid(row=4, column=3, sticky="EW")

add_password = Button(text="Add", command=add_pass, width=34, highlightthickness=0)
add_password.grid(row=5, column=2, columnspan=2)

window.mainloop()