import tkinter as tk
import random
import pyperclip

class PasswordGenerator:
    def __init__(self, master):
        # Initialize the GUI components
        self.master = master
        master.title("Password Generator")
        master.geometry("300x250")

        # Create a label and entry field for the password length
        self.length_label = tk.Label(master, text="Password Length (8-15):")
        self.length_label.pack()
        self.length_entry = tk.Entry(master, width=20)
        self.length_entry.pack()

        # Create checkboxes for including uppercase letters, numbers, and special characters
        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbox = tk.Checkbutton(master, text="Include Uppercase Letters", variable=self.uppercase_var, command=lambda: self.update_checkbox(self.uppercase_checkbox, self.uppercase_var))
        self.uppercase_checkbox.pack()

        self.numbers_var = tk.IntVar()
        self.numbers_checkbox = tk.Checkbutton(master, text="Include Numbers", variable=self.numbers_var, command=lambda: self.update_checkbox(self.numbers_checkbox, self.numbers_var))
        self.numbers_checkbox.pack()

        self.special_chars_var = tk.IntVar()
        self.special_chars_checkbox = tk.Checkbutton(master, text="Include Special Characters", variable=self.special_chars_var, command=lambda: self.update_checkbox(self.special_chars_checkbox, self.special_chars_var))
        self.special_chars_checkbox.pack()

        # Create a button to generate the password
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        # Create a label and entry field to display the generated password
        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, width=20)
        self.password_entry.pack()

        # Create a button to copy the generated password
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_password)
        self.copy_button.pack()

        # Create an animation label to display a message when the password is generated
        self.animation_label = tk.Label(master, text="", fg="green")
        self.animation_label.pack()

    def update_checkbox(self, checkbox, var):
        if var.get():
            checkbox.config(fg="green")
        else:
            checkbox.config(fg="black")

    def generate_password(self):
        # Get the password length and options from the GUI components
        try:
            length = int(self.length_entry.get())
        except ValueError:
            self.animation_label.config(text="Invalid password length. Please enter a number.", fg="red")
            return

        if length < 8 or length > 15:
            self.animation_label.config(text="Password length should be between 8 and 15 characters.", fg="red")
            return

        has_uppercase = self.uppercase_var.get()
        has_numbers = self.numbers_var.get()
        has_special_chars = self.special_chars_var.get()

        # Define the character sets to use for the password
        chars = "abcdefghijklmnopqrstuvwxyz"
        if has_uppercase:
            chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if has_numbers:
            chars += "0123456789"
        if has_special_chars:
            chars += "!@#$%^&*()_-+={}[]:;<>,./?"

        # Generate the password
        password = "".join(random.choice(chars) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

        # Display a success message
        self.animation_label.config(text="Password generated!", fg="green")

    def copy_password(self):
        password = self.password_entry.get()
        pyperclip.copy(password)
        self.animation_label.config(text="Password copied to clipboard!", fg="green")

# Create the GUI
root = tk.Tk()
my_gui = PasswordGenerator(root)
root.mainloop()