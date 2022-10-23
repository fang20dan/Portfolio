"""Venmo Class"""
import requests
import json
from venmo_api import Client

class venmo:
    """headers = user agent (just google what is my user agent and paste it"""
    """"""
    def __init__(self, access_token, headers):
        self.access_token = access_token
        self.headers = headers
        self.baseRoute = "https://api.venmo.com/v1/me?"
        

    def getParams(self):
        print(self.params)

    
    def getBalance(self) -> float: 
        headers = {'User-Agent': self.headers}
        params = {"access_token" : self.access_token}  
        response = requests.get(self.baseRoute, headers = headers, params = params)
        if(response.status_code == 200):
            """print("SUCCESS!!!!")"""
            response = response.json()
            tempBal = response['data']['balance']
            balance = float(tempBal)
            return balance

        else:
            print(f"FAILED REQUEST: {response.status_code}")
            print(response.text)
            return 9.0

    @staticmethod
    def getMyAccessToken():
        print("Enter Venmo Credentials In Order to View Balance")
        username = ("Enter Your Venmo Username: ")
        password = ("Enter Your Venmo Password: ")
        access_token = Client.get_access_token(username= username,
                                        password= password)
        print("My token:", access_token)
        print("Remember to save this access token!!")


myVenmo = venmo('3ef9d12ddcb14dfbc07e21b06ee4cdbeb8625d8b611bca95a7e26bf069f0b5d3', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0) Gecko/20100101 Firefox/103.0')
print(myVenmo.getBalance())


    
