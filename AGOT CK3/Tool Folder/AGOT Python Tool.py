#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
import subprocess

def run_greathouses_notebook():
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "script", r"C:\Users\jmpmc\Python\AGOT CK3\Great Houses Updater.ipynb"], check=True)
        subprocess.run(["python", r"C:\Users\jmpmc\Python\AGOT CK3\Great Houses Updater.py"], check=True)
        messagebox.showinfo("Success", "characters from Great Houses successfully updated.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to update  characters from the great Houses.")

def run_river_notebook():
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "script", r"C:\Users\jmpmc\Python\AGOT CK3\Riverlords Updater.ipynb"], check=True)
        subprocess.run(["python", r"C:\Users\jmpmc\Python\AGOT CK3\Riverlords Updater.py"], check=True)
        messagebox.showinfo("Success", "Riverlands characters successfully updated.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to update Riverlands characters.")
        
def run_river2_notebook():
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "script", r"C:\Users\jmpmc\Python\AGOT CK3\Riverlords Updater 2.ipynb"], check=True)
        subprocess.run(["python", r"C:\Users\jmpmc\Python\AGOT CK3\Riverlords Updater 2.py"], check=True)
        messagebox.showinfo("Success", "Riverlands characters successfully updated 2.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to update Riverlands characters 2.")

def run_northern_notebook():
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "script", r"C:\Users\jmpmc\Python\AGOT CK3\Northern Lords Updater.ipynb"], check=True)
        subprocess.run(["python", r"C:\Users\jmpmc\Python\AGOT CK3\Northern Lords Updater.py"], check=True)
        messagebox.showinfo("Success", "Northern characters successfully updated.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to update northern characters.")

def run_northern2_notebook():
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "script", r"C:\Users\jmpmc\Python\AGOT CK3\Northern Lords Updater 2.ipynb"], check=True)
        subprocess.run(["python", r"C:\Users\jmpmc\Python\AGOT CK3\Northern Lords Updater 2.py"], check=True)
        messagebox.showinfo("Success", "Northern characters successfully updated.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to update northern characters.")

def run_vale_c_notebook():
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "script", r"C:\Users\jmpmc\Python\AGOT CK3\Vale Updater.ipynb"], check=True)
        subprocess.run(["python", r"C:\Users\jmpmc\Python\AGOT CK3\Vale Updater.py"], check=True)
        messagebox.showinfo("Success", "Vale characters successfully updated.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to update northern characters.")

def run_west_c_notebook():
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "script", r"C:\Users\jmpmc\Python\AGOT CK3\Westerlands Updater.ipynb"], check=True)
        subprocess.run(["python", r"C:\Users\jmpmc\Python\AGOT CK3\Westerlands Updater.py"], check=True)
        messagebox.showinfo("Success", "Westerlands characters successfully updated.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to update western characters.")

def run_iron_c_notebook():
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "script", r"C:\Users\jmpmc\Python\AGOT CK3\Iron Updater.ipynb"], check=True)
        subprocess.run(["python", r"C:\Users\jmpmc\Python\AGOT CK3\Iron Updater.py"], check=True)
        messagebox.showinfo("Success", "Iron characters successfully updated.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to update Iron characters.")

def run_crown_c_notebook():
    try:
        subprocess.run(["jupyter", "nbconvert", "--to", "script", r"C:\Users\jmpmc\Python\AGOT CK3\Crownlands Updater.ipynb"], check=True)
        subprocess.run(["python", r"C:\Users\jmpmc\Python\AGOT CK3\Crownlands Updater.py"], check=True)
        messagebox.showinfo("Success", "Crownlands characters successfully updated.")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to update Crownlands characters.")

# Create the main window
root = tk.Tk()
root.title("AGOT Characters Updater")

# Set window size and position
window_width = 1000
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Customize window background color
root.configure(bg="lightgray")

# Customize button appearance
button_style = {
    "bg": "red",
    "fg": "black",
    "font": ("Calibri", 10),
    "borderwidth": 8,
    "width": 50,
    "height": 3,
    "activebackground": "skyblue"
}

# Create buttons to trigger the executions
gh_button = tk.Button(root, text="Update Characters from the Great Houses", command=run_greathouses_notebook, **button_style)
gh_button.grid(row=0, column=0, padx=10, pady=10)

river_button = tk.Button(root, text="Update Riverlands Characters", command=run_river_notebook, **button_style)
river_button.grid(row=1, column=0, padx=10, pady=10)

river2_button = tk.Button(root, text="Update 2nd Batch Riverlands Characters", command=run_river2_notebook, **button_style)
river2_button.grid(row=2, column=0, padx=10, pady=10)

northern_button = tk.Button(root, text="Update Northern Characters", command=run_northern_notebook, **button_style)
northern_button.grid(row=3, column=0, padx=10, pady=10)

northern2_button = tk.Button(root, text="Update 2nd Batch of Northern Characters", command=run_northern2_notebook, **button_style)
northern2_button.grid(row=4, column=0, padx=10, pady=10)

vale_button = tk.Button(root, text="Update Vale Characters", command=run_vale_c_notebook, **button_style)
vale_button.grid(row=0, column=1, padx=10, pady=10)

west_button = tk.Button(root, text="Update Westerlands Characters", command=run_west_c_notebook, **button_style)
west_button.grid(row=1, column=1, padx=10, pady=10)

iron_button = tk.Button(root, text="Update Ironborn Characters", command=run_iron_c_notebook, **button_style)
iron_button.grid(row=2, column=1, padx=10, pady=10)

crown_button = tk.Button(root, text="Update Crownlands Characters", command=run_crown_c_notebook, **button_style)
crown_button.grid(row=2, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()


# In[34]:


from tkinter import Tk, font
root = Tk()
font.families()


# In[ ]:




