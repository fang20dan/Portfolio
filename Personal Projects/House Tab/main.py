from doctest import master
from ArduinoClass import *
from VenmoClass import *
from tkinter import *
import tkinter
import customtkinter



def main(): 
    global drinkText
    myController = arduino()
   
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    
    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("400x400")


    # Use CTkButton instead of tkinter Button
    pourButton = customtkinter.CTkButton(master=app, text="Pour!", command = myController.pour, width = 150, height = 40, hover_color="#99badd")
    refillButton = customtkinter.CTkButton(master=app, text="Refill Machine", command = myController.refilled, width = 150, height = 40, hover_color="#99badd")
    #startButton = customtkinter.CTkButton(master=app, text="Refill Machine", command = myController.start, width = 50, height = 50, hover_color="#99badd")
    drinkText = customtkinter.CTkLabel(master=app, text = "Drink Credits: " + str(myController.getDrinkCredits()), width = 120, height = 25, corner_radius = 8)
    refreshButton = customtkinter.CTkButton(master = app, text = "Update Drink Credits", command = myController.isPaid, width = 150, height = 40, hover_color="#99badd")
   
    
    drinkText.place(relx = 0.5, rely = 0.40, anchor=tkinter.CENTER)
    #startButton.place(relx= 0.25, rely = 0.8, anchor= tkinter.CENTER)
    pourButton.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
    refillButton.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
    refreshButton.place(relx=0.5, rely=.8, anchor=tkinter.CENTER)
   
    def update_clock(appl):
        appl.drinkText.configure(text = "Drink Credits: " + str(myController.credits))
        appl.after(1000, update_clock)
    
    
    def textLoad():
        #drinkText = customtkinter.CTkLabel(master=app, text = "Drink Credits: " + str(myController.drinks), width = 120, height = 25, corner_radius = 8)
        drinkText.configure(text = "Drink Credits: " + str(myController.credits))
        app.after(100,textLoad)
        update_clock(app)
    
    
    app.after(100, textLoad)
    app.mainloop()
    

    


if __name__ == "__main__":
    main()