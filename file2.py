from tkinter import *
from tkinter import messagebox

# Create a window
window = Tk()
window.title("Login ")
window.geometry("500x350")

# Set the background color of the window
window.config(bg="purple")

# Create a label for the username
username_label = Label(window, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=10)

# Create an entry box for the username
username_entry = Entry(window)
username_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a label for the password
password_label = Label(window, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)

# Create an entry box for the password
password_entry = Entry(window, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Define a function to check the login credentials
def check_login():
    # Get the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password are correct
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Error", "Incorrect username or password.")

# Create a button to submit the login credentials
login_button = Button(window, text="Login", command=check_login)
login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the window
window.mainloop()
