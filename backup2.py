import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image

def getvals():
    print("Accepted too of course")



root = ctk.CTk()
root_width = 500
root_height = 500
root.geometry(f"{root_width}x{root_height}")
root.title("Parking Management System")

#Form lable
img1=ImageTk.PhotoImage(Image.open("logo.png"))
Label_frame = ctk.CTkLabel(root, text ="Registraton Form", font = ("ar", 15, "bold"), image=img1).pack(padx=20, pady=20, fill=ctk.BOTH, expand=True)

left_half_canvas = ctk.CTkFrame(Label_frame)
# left_half_canvas = ctk.CTkFrame(Label_frame).place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Label = tk.Label(root, text ="Packing Registraton Form", font = "ar 15 bold").grid(row=0, column=0)
# canvas_frame=ctk.CTkFrame(left_half,width=root_width*0.75, height = root_height*0.75).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# canvas_frame=ctk.CTkFrame(left_half_canvas).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

group_1 = ctk.CTkFrame(left_half_canvas)
group_2 = ctk.CTkFrame(left_half_canvas)
group_3 = ctk.CTkFrame(left_half_canvas)
group_4 = ctk.CTkFrame(left_half_canvas)
group_5 = ctk.CTkFrame(left_half_canvas)
group_6 = ctk.CTkFrame(left_half_canvas)

#Form fields names and packing
# name = ctk.CTkLabel(group_1, text ="Name").place(relx=0.1, rely=0.5, anchor=tk.W)
name = ctk.CTkLabel(group_1, text ="Name").pack(side=tk.LEFT, padx=5, pady=5, fill=ctk.X, expand=True)
phone = ctk.CTkLabel(group_2, text ="Phone").pack(side=tk.LEFT, padx=5, pady=5, fill=ctk.X, expand=True)
gender = ctk.CTkLabel(group_3, text ="Gender").pack(side=tk.LEFT, padx=5, pady=5, fill=ctk.X, expand=True)
emergency = ctk.CTkLabel(group_4, text ="Emergency").pack(side=tk.LEFT, padx=5, pady=5, fill=ctk.X, expand=True)
paymentmode = ctk.CTkLabel(group_5, text ="Payment Mode").pack(side=tk.LEFT, padx=5, pady=5, fill=ctk.X, expand=True)

#Declaring form entry fields
namevalue = tk.StringVar()
phonevalue = tk.StringVar()
gendervalue = tk.StringVar()
emergencyvalue = tk.StringVar()
paymentmodevalue = tk.StringVar()
checkvalue = tk.IntVar()

#Form entry fiels and packing
# nameentry = ctk.CTkEntry(left_half_canvas, textvariable= namevalue).grid(row=1, column=2)
nameentry = ctk.CTkEntry(group_1, textvariable=namevalue).pack(padx=5, pady=5, fill=ctk.X, expand=True)

phoneentry = ctk.CTkEntry(group_2, textvariable= phonevalue).pack(padx=5, pady=5, fill=ctk.X, expand=True)
genderentry = ctk.CTkEntry(group_3, textvariable= gendervalue).pack(padx=5, pady=5, fill=ctk.X, expand=True)
emergencyentry = ctk.CTkEntry(group_4, textvariable= emergencyvalue).pack(padx=5, pady=5, fill=ctk.X, expand=True)
paymentmodeentry = ctk.CTkEntry(group_5, textvariable= paymentmodevalue).pack(padx=5, pady=5, fill=ctk.X, expand=True)

# Creating Checkbox
checkbtn = ctk.CTkCheckBox(group_6, text="remember me?", variable=checkvalue).pack(side=tk.LEFT, padx=5, pady=5, fill=ctk.X, expand=True)

# Submit button
submit_button = ctk.CTkButton(group_6, text="Submit", command=getvals).pack(side=tk.LEFT, padx=5, pady=5, fill=ctk.X, expand=True)

# combined_halves.pack()
# left_half.pack()



group_1.pack(padx=5, pady=2, fill=ctk.X, expand=True)
group_2.pack(padx=5, pady=2, fill=ctk.X, expand=True)
group_3.pack(padx=5, pady=2, fill=ctk.X, expand=True)
group_4.pack(padx=5, pady=2, fill=ctk.X, expand=True)
group_5.pack(padx=5, pady=2, fill=ctk.X, expand=True)
group_6.pack(padx=5, pady=2, fill=ctk.BOTH, expand=True)


left_half_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# right_half.pack(side='left',padx=5, pady=5, fill=ctk.BOTH, expand=True)
# combined_halves.pack(padx=10, pady=10, fill=ctk.BOTH, expand=True)


root.mainloop()



