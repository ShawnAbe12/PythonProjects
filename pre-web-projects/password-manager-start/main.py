from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def search_file():
    try:
        with open("data.json") as file:
            data = json.load(file)
            print(data[website_entry.get()])
    except KeyError or FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found.")
    else:
        messagebox.showinfo(title=website_entry.get(), message=f"Email: {data[website_entry.get()]['email']}"
                                                               f"\nPassword: {data[website_entry.get()]['password']}")
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = []
    password += [char for char in password_list]

    password = "".join(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    password_entry.clipboard_clear()
    password_entry.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    user = user_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }
    # print(user,website,password)

    if len(website) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        is_ok = False
    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user}"
    #                                                           f"\nPassword: {password}"
    #                                                           f"\nIs it ok to save?")
    else:
        try:
            with open("data.json", "r") as file:
                # file.write(f"{website} | {user} | {password}\n")
                # json.dump(new_data, file, indent=4)
                data = json.load(file)
                # print(data)
                data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data,file,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)

website_label = Label(text="Website: ")
user_label = Label(text="Email/Username: ")
password_label = Label(text="Password: ")

website_entry = Entry(width=21)
user_entry = Entry(width=39)
password_entry = Entry(width=21)

search_button = Button(text="Search", command=search_file)
gen_pass_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=save)

canvas.create_image(100, 100, image=image)

canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
user_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1)
website_entry.focus()

user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "johnabe5605@gmail.com")
password_entry.grid(column=1, row=3)

search_button.grid(column=2, row= 1, columnspan=2)
gen_pass_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
