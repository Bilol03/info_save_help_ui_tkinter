import string
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import pyperclip
import string
from random import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    nr_letters = randint(5, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)

    if paswd_input.get != "":
        paswd_input.delete(0, END)
    length = randint(8, 15)
    res = []
    for i in range(nr_letters):
        res.append(choice(string.ascii_letters))
    for i in range(nr_symbols):
        res.append(choice(string.punctuation))
    for i in range(nr_numbers):
        res.append(choice(string.digits))

    res = ''.join(sample(res, len(res)))
    paswd_input.insert(0, res)
    pyperclip.copy(res)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    file = open('data.txt', 'a')
    website = web_input.get()
    password = paswd_input.get()
    email = email_input.get()


    if website == "":
        messagebox.showerror(title="Oops", message="Please fill the website input!!!")
    elif paswd_input == "":
        messagebox.showerror(title="Oops", message="Please enter the password!!!")
    else:
        file.write(f"{website}  |  {email}  |  {password} \n")
        web_input.delete(0, END)
        password.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Generator')
window.config(width=600, height=600, background='white', padx=20, pady=20)

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


web_title = Label(text='Website:', highlightthickness=0, background='white', fg='black', font=('Roboto sans-serif', 13))
web_title.grid(column=0, row=1)

web_input = Entry(width=35, highlightbackground='white', fg='black', bg='white')
web_input.grid(column=1, row=1, columnspan=2)

email_username = Label(text='Email/Username:', highlightthickness=0, bg='white', fg='black', font=('Roboto sans-serif', 13))
email_username.grid(column=0, row=2)

email_input = Entry(width=35, highlightbackground='white', fg='black', bg='white')
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'example@gmail.com')

passwd = Label(text='Password:', highlightthickness=0, bg='white', fg='black', font=('Roboto sans-serif', 13))
passwd.grid(column=0, row=3)

paswd_input = Entry(width=20, highlightbackground='white', fg='black', bg='white')
paswd_input.grid(column=1, row=3)

passwd_generator = Button(width=10, text='Generate', highlightthickness=0, highlightbackground='white', command=generator)
passwd_generator.grid(column=2, row=3)

add_button = Button(text='Add', width=36, highlightthickness=0, highlightbackground='white', command=save_password)
add_button.grid(column=1, row=4, columnspan=3)
window.mainloop()


