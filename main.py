import json
from tkinter import *
from tkinter import messagebox
from password import *

# main window = Tk()
window = Tk()
window.title("Password Manager")
window.config(width=200, height=200, padx=60, pady=60)

# website
website_label = Label(text='Website', font=('Calibre', 12, 'normal'))
website_label.grid(row=1, column=0)

# website entry -> appends data to new
website_entry = Entry()
website_entry.focus()
website_entry.config(width=43)
website_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# username/emai Label()
username_label = Label(text='Username / e-mail', font=('Calibre', 12, 'normal'))
username_label.grid(row=2, column=0)

# username_entry Entry()
username_entry = Entry(width=43)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'test.me@testmail.com')

# password Label()
password_label = Label(text='Password', font=("Calibre", 12, 'normal'))
password_label.grid(row=3, column=0)

# password Entry()
password_entry = Entry()
password_entry.grid(row=3, column=1)


# add to list (tmp); will be changed to add to a file or .cvs

# button generate
def set_text(text):  # function to insert text into Entry()
    password_entry.delete(0, END)
    password_entry.insert(0, text)
    return


generate_button = Button(text='Generate password', command=lambda: set_text(generate_pass()))
generate_button.grid(row=3, column=2)


# button for Adding data into txt file
def add_to_file():
    website_a = website_entry.get()
    username_a = username_entry.get()
    password_a = password_entry.get()
    new_data = {
        website_a: {
            "email": username_a,
            "password": password_a
        }
    }

    if len(website_a) == 0 or len(password_a) == 0:
        messagebox.showinfo(title="Error!!!", message='You lack some information in your input!')
    else:
        if len(password_a) < 12:
            messagebox.showwarning(title='Password error',
                                   message='Your password is less than 12 characters. \nPlease try again!\n')
        else:
            try:
                with open('password_saved.json', 'r') as file:
                    # read old data
                    data = json.load(file)
            except FileNotFoundError:
                with open('password_saved.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                # update old data with new data
                data.update(new_data)

                with open('password_saved.json', 'w') as file:
                    # save updated data
                    json.dump(new_data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                # username_entry.delete(0, END)
                password_entry.delete(0, END)


add_bttn = Button(text='Add', command=add_to_file, width=35)
add_bttn.grid(row=4, column=1, columnspan=2, padx=20, pady=20)

window.mainloop()
