import tkinter as tk
import customtkinter as ctk
from customtkinter import CTk, CTkLabel, CTkEntry, CTkCheckBox, CTkButton
from PIL import ImageTk, Image

def on_entry_click(entry, default_text, default_color='black'):
    if entry.get() == default_text:
        entry.delete(0, tk.END)
        entry.insert(0, default_text)
        entry.tag_configure("default_color", foreground=default_color)

def on_focus_out(entry, default_text, default_color='grey'):
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.tag_configure("default_color", foreground=default_color)

def getvals():
    print("Accepted too of course")

root = CTk()
root_width = 500
root_height = 500
root.geometry(f"{root_width}x{root_height}")
root.title("Parking Management System")

# Form label
img1 = ctk.CTkImage(Image.open("logo.png"))
Label_frame = CTkLabel(root, text="Registration Form", font=("ar", 15, "bold"), image=img1)
Label_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

left_half_canvas = ctk.CTkFrame(Label_frame)

group_1 = ctk.CTkFrame(left_half_canvas)
group_2 = ctk.CTkFrame(left_half_canvas)
group_3 = ctk.CTkFrame(left_half_canvas)
group_4 = ctk.CTkFrame(left_half_canvas)
group_5 = ctk.CTkFrame(left_half_canvas)
group_6 = ctk.CTkFrame(left_half_canvas)

# Form fields names and packing
field_labels = ["Name", "Phone", "Gender", "Emergency", "Payment Mode"]
entry_variables = [tk.StringVar() for _ in range(len(field_labels))]

for i, label_text in enumerate(field_labels):
    label = CTkLabel(eval(f"group_{i + 1}"), text=label_text)
    label.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

# Form entry fields and packing
default_texts = ["Name goes here", "Phone goes here", "Gender goes here", "Emergency goes here", "Payment Mode goes here"]
entries = [CTkEntry(eval(f"group_{i + 1}"), textvariable=entry_variables[i]) for i in range(len(field_labels))]

for i, entry in enumerate(entries):
    entry.insert(0, default_texts[i])
    entry.tag_configure("default_color", foreground='grey')  # Initial color
    entry.pack(padx=5, pady=5, fill=tk.X, expand=True)
    entry.bind('<FocusIn>', lambda event, index=i: on_entry_click(entries[index], default_texts[index]))
    entry.bind('<FocusOut>', lambda event, index=i: on_focus_out(entries[index], default_texts[index]))

# Creating Checkbox
checkvalue = tk.IntVar()
checkbtn = CTkCheckBox(group_6, text="Remember me?", variable=checkvalue)
checkbtn.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

# Submit button
submit_button = CTkButton(group_6, text="Submit", command=getvals)
submit_button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

groups = [group_1, group_2, group_3, group_4, group_5, group_6]
for group in groups:
    group.pack(padx=5, pady=2, fill=tk.X, expand=True)

left_half_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
root.mainloop()
