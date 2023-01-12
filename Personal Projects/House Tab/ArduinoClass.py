from base64 import b16decode
from tkinter import *
from tokenize import String
from xmlrpc.client import Boolean, boolean
import pyfirmata
import time
from VenmoClass import *
import math
import threading
from main import *
import customtkinter
import tkinter

class arduino:
    
    def __init__(self):
        self.credits = 0
        self.drinks_poured = 0
        self.maxDrinks = 40
        self.price = 1
        self.canPour = TRUE
        self.board = pyfirmata.Arduino('COM3')
        self.myVenmo = venmo('3ef9d12ddcb14dfbc07e21b06ee4cdbeb8625d8b611bca95a7e26bf069f0b5d3', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0')
        self.b1 = 0
        #myVenmo.getBalance()
        self.b2 = self.b1
        
        

    def pour(self):
        #if paid and there are drinks left
        if self.canPour & self.isPaid() & (not self.noMoreDrinks()) & (self.credits > 0):
            self.canPour = FALSE
            self.board.digital[13].write(1)
            time.sleep(4)
            self.board.digital[13].write(0)
            time.sleep(1)
            self.credits -= 1
            self.drinks_poured += 1
            self.canPour = TRUE
            print(self.credits)
            print(self.drinks_poured)
        #commenting section out until know the reason will made this
            """
        elif self.canPour & (not self.isPaid()) & (not self.noMoreDrinks()) & (self.drinks > 0):
            self.canPour = FALSE
            self.board.digital[13].write(1)
            time.sleep(4)
            self.board.digital[13].write(0)
            time.sleep(1)
            self.drinks -= 1
            self.drinks_poured += 1
            self.canPour = TRUE
            print(self.drinks)
            print(self.drinks_poured)
        """    
        else: 
            print("Sorry Not Enough Money In Account")
        
    #should create class for drinks (price/name) so can use to calculate credits
    def isPaid(self) -> boolean:
        """Determines if balance has changed by an increment greater than or equal to the cost of a drink"""
        self.b2 = myVenmo.getBalance()
        diff = self.b2 - self.b1
        if(diff >= self.price):
            #assuming drinks are directly correlated with $1
            math.floor(diff)
            self.credits += diff
            self.b1 = self.b2
            return TRUE
        else:
            return FALSE
        
    def refilled(self):
        """Hit refill button with an if statement if password is entered correctly the user is given the option to prime the machine"""
        authen = Tk()
        authen.geometry("450x300")
        def check():
            test = password_entry.get()
            if test == "urisucks":
                self.drinks_poured = 0
                authen.destroy()
                print(self.drinks_poured)
                primeWindow = Tk()
                primeWindow.geometry("450x300")
                primeButton = customtkinter.CTkButton(master = primeWindow, text = "prime", command = self.primeMachine, width = 70, height = 40, hover_color="#99badd")
                primeButton.pack(pady = 50)
               
            return None 
        password = StringVar()
        password_entry = Entry(authen)
        password_entry.pack()
        submit = Button(authen, text = "Submit", command = check).pack()

    def noMoreDrinks(self) -> boolean:
        
        if self.drinks_poured == self.maxDrinks:
            return TRUE
        else:
            return FALSE
            """Throw Message on screen to refill"""
    """ def start(self):        
        while True:
            print("test")
            time.sleep(5) """
    
    def getDrinkCredits(self) -> int:
        return self.credits
    
    def primeMachine(self):
        self.board.digital[13].write(1)
        time.sleep(5)
        self.board.digital[13].write(0)
        time.sleep(.1)
        
        
        
    

