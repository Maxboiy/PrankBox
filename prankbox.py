import tkinter
import customtkinter
from tkinter import messagebox

app = customtkinter.CTk()
app.geometry("400x600")
app.title("PrankBox - MBD Silly Project")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(fill="both", expand=True)

label_name = customtkinter.CTkLabel(text="PrankBox", master=frame_1, justify=tkinter.LEFT)
label_name.pack(padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Title") # This will be the title of the pop-up box / the name
entry_1.pack(pady=12, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Message") # and this will be the contents of the pop-up box
entry_2.pack(pady=12, padx=10)

label_1 = customtkinter.CTkLabel(master=frame_1,text="Type of icon", justify=tkinter.LEFT)
label_1.pack(pady=1, padx=10)

combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Error", "Warning", "Info"])
combobox_1.pack(pady=12, padx=10)

label_4 = customtkinter.CTkLabel(text="Will arrive soon!", master=frame_1, justify=tkinter.LEFT)
label_4.pack(padx=10)

combobox_2 = customtkinter.CTkComboBox(frame_1, values=["Yes and No", "Ok and Cancel", "Yes, No and Cancel", "Retry and Cancel"])
combobox_2.pack(pady=12, padx=10)

normal = customtkinter.CTkCheckBox(text="Customize the buttons", master=frame_1)
normal.pack(pady=12, padx=10)

# This is the save changes button
def change_settings():
    # print("button passed") This is for troubleshooting if the button doesn't work
    seekforchange = normal.get()
    if seekforchange == True:
        # print("seekforchange passed") This is for troubleshooting if the button doesn't work
        combobox_1.configure(state="disabled")
        combobox_2.configure(state="normal")

    elif seekforchange == False:
        combobox_1.configure(state="normal")
        combobox_2.configure(state="disabled")

label_3 = customtkinter.CTkLabel(text="Please press Apply when you checked the checkbox", master=frame_1, justify=tkinter.LEFT)
label_3.pack(padx=10)

button_apply = customtkinter.CTkButton(text="Apply changes", master=frame_1, command=change_settings) # This is the button that will create the pop-up box and if selected make the program go invisible
button_apply.pack(pady=12, padx=10)

switch_1 = customtkinter.CTkSwitch(text="Make the program go invisible", master=frame_1)
switch_1.pack(pady=12, padx=10)

# This is the button that makes the pop-up without it this program is useless
def button_callback():
    checker = combobox_1.get() # This will check which value the Combobox is
    invisable = switch_1.get() # and this will check the switch thing and if the value is 1 the program will go invisible
    # If the Switch is selected this code will activate instead of that less cooler code under me
    if invisable == True:
        if checker == "Error":
            app.withdraw()
            messagebox.showerror(entry_1.get(), entry_2.get())

        elif checker == "Warning":
            app.withdraw()
            messagebox.showwarning(entry_1.get(), entry_2.get())

        elif checker == "Info":
            app.withdraw()
            messagebox.showinfo(entry_1.get(), entry_2.get())

        app.destroy()
        app.quit()
            
    # If the Switch is not selected this code will activate
    if invisable == False:
        if checker == "Error":
            messagebox.showerror(entry_1.get(), entry_2.get())

        elif checker == "Warning":
            messagebox.showwarning(entry_1.get(), entry_2.get())

        elif checker == "Info":
            messagebox.showinfo(entry_1.get(), entry_2.get())

        app.destroy()
        app.quit()

# print(entry_1.get(), entry_2.get())
# This is for troubleshooting! Change the entry_1 and _2 to which element you want and see which value it makes

button_1 = customtkinter.CTkButton(text="Create", master=frame_1, command=button_callback) # This is the button that will create the pop-up box and if selected make the program go invisible
button_1.pack(pady=12, padx=10)

label_1 = customtkinter.CTkLabel(text="PrankBox   |   Version:1.0 Beta   |   a MBD Project   |   M6-D6-Y2024", master=frame_1, justify=tkinter.LEFT)
label_1.pack(padx=10)

label_2 = customtkinter.CTkLabel(text="WARNING: Program will close after the pop-up is closed!", master=frame_1, justify=tkinter.LEFT)
label_2.pack(padx=10)

combobox_2.configure(state="disabled")
normal.configure(state="disabled")
button_apply.configure(state="disabled")

app.mainloop()
