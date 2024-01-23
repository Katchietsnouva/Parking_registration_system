import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image

def getvals():
    print("Accepted too, of course")

root = ctk.CTk()
root_width = 400
root_height = 400
root.geometry(f"{root_width}x{root_height}")
root.title("Parking Management System")

# Form label
img1 = ImageTk.PhotoImage(Image.open("logo.png"))
Label_frame = ctk.CTkLabel(root, text="Registration Form", font=("ar", 15, "bold"), image=img1)
Label_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Left half canvas
left_half_canvas = ctk.CTkFrame(Label_frame)
left_half_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Form fields names and packing using place
name = ctk.CTkLabel(left_half_canvas, text="Name").pack()
# name = ctk.CTkLabel(left_half_canvas, text="Name").place(relx=0.5, rely=0.1, anchor=tk.CENTER)
phone = ctk.CTkLabel(left_half_canvas, text="Phone").place(relx=0.5, rely=0.25, anchor=tk.CENTER)
gender = ctk.CTkLabel(left_half_canvas, text="Gender").place(relx=0.5, rely=0.4, anchor=tk.CENTER)
emergency = ctk.CTkLabel(left_half_canvas, text="Emergency").place(relx=0.5, rely=0.55, anchor=tk.CENTER)
paymentmode = ctk.CTkLabel(left_half_canvas, text="Payment Mode").place(relx=0.5, rely=0.7, anchor=tk.CENTER)

root.mainloop()


# import tkinter as tk
# import customtkinter as ctk
# from PIL import ImageTk, Image

# def getvals():
#     print("Accepted too of course")

# root = ctk.CTk()
# root_width = 400
# root_height = 400
# root.geometry(f"{root_width}x{root_height}")
# root.title("Parking Management System")

# #Form lable
# img1=ImageTk.PhotoImage(Image.open("logo.png"))
# Label_frame = ctk.CTkLabel(root, text ="Registraton Form", font = ("ar", 15, "bold"), image=img1).pack()
# # Label = tk.Label(root, text ="Packing Registraton Form", font = "ar 15 bold").grid(row=0, column=0)
# # canvas_frame=ctk.CTkFrame(left_half,width=root_width*0.75, height = root_height*0.75).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# left_half_canvas = ctk.CTkFrame(Label_frame).place(relx=0.5, rely=0.1, anchor=tk.CENTER)
# # canvas_frame=ctk.CTkFrame(left_half_canvas).place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# #Form fields names and packing
# name = ctk.CTkLabel(left_half_canvas, text ="Name").place(relx=0.1, rely=0.5, anchor=tk.W)
# phone = ctk.CTkLabel(left_half_canvas, text ="Phone").pack()
# gender = ctk.CTkLabel(left_half_canvas, text ="Gender").pack()
# emergency = ctk.CTkLabel(left_half_canvas, text ="Emergency").pack()
# paymentmode = ctk.CTkLabel(left_half_canvas, text ="Payment Mode").pack()

# #Declaring form entry fields
# namevalue = tk.StringVar(value= "name goes here")
# phonevalue = tk.StringVar()
# gendervalue = tk.StringVar()
# emergencyvalue = tk.StringVar()
# paymentmodevalue = tk.StringVar()
# checkvalue = tk.IntVar()

# #Form entry fiels and packing
# # nameentry = ctk.CTkEntry(left_half_canvas, textvariable= namevalue).grid(row=1, column=2)
# nameentry = ctk.CTkEntry(left_half_canvas, textvariable=namevalue).pack()
# phoneentry = ctk.CTkEntry(left_half_canvas, textvariable= phonevalue).pack()
# genderentry = ctk.CTkEntry(left_half_canvas, textvariable= gendervalue).pack()
# emergencyentry = ctk.CTkEntry(left_half_canvas, textvariable= emergencyvalue).pack()
# paymentmodeentry = ctk.CTkEntry(left_half_canvas, textvariable= paymentmodevalue).pack()

# # Creating Checkbox
# checkbtn = ctk.CTkCheckBox(left_half_canvas, text="remember me?", variable=checkvalue).pack()

# # Submit button
# submit_button = ctk.CTkButton(left_half_canvas, text="Submit", command=getvals).pack()

# # combined_halves.pack()
# # left_half.pack()
# root.mainloop()