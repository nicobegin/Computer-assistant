#!/usr/bin/env python

"""
This code is used to create a software to facilitate the use of computer for older people by checking their connexion, creating shortcut etc ...
We assume that the user is operating on Windows
Constants are meant to be personnal and to be changed depending on the people using it
More settings incomings
How to run : Only run the script and the GUI will appear. 
"""


#-----------------------------------------------------------------------------#
#                              Python script                                  #
#-----------------------------------------------------------------------------#

__author__  = 'Nicolas Begin'
__version__ = 1.0

#-----------------------------------------------------------------------------#
#                              System imports                                 #
#-----------------------------------------------------------------------------#


from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 

import requests ## wifi connection
import webbrowser #To open an url

import sys
import os #Command line to get wifi connexion
import subprocess
import platform

import time


#-----------------------------------------------------------------------------#
#                             Constant definition                             #
#-----------------------------------------------------------------------------#

MAIL_URL = "https://login.yahoo.com/"
TAXES_URL = "https://www.impots.gouv.fr/portail/"
PATH_TO_USB = ""
WIFI_ID = "Michel"
WIFI_ID_BIS = "trouville"
WIFI_PASSWORD = "bar"
#MAIN_URL =

#-----------------------------------------------------------------------------#
#                                    Code                                     #
#-----------------------------------------------------------------------------#




class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        ## Display settings
        self.setGeometry(100, 100, 800, 600) #X,Y, width, height
        self.setWindowTitle("Assistance informatique") #set title
        

        self.button_creation_test()
        self.button_creation_shortcut_mail()
        self.button_creation_shortcut_taxes()
        self.button_creation_shortcut_wifi()
        self.show() #display

    ## Create the button for internet test
    def button_creation_test(self):
        button_internet = QPushButton('Test internet', self)
        button_internet.setGeometry(200, 200, 300, 50)
        button_internet.clicked.connect(self.internet_clicked)


    ## Display the result of the test with a message box
    def internet_clicked(self): 
        alert = QMessageBox()
        
        if self.is_connected() == False:
            alert.setText('Vous n\'êtes pas connecté à internet')
        else : 
            alert.setText('Vous avez accès à internet')
        alert.exec()

    ## Test of the connection by attempting to access a website
    def is_connected(self): 
        timeout = 5

        try:
            request = requests.get(MAIL_URL, timeout=timeout)
            return True

        except (requests.ConnectionError, requests.Timeout) as exception:
            return False

    ## Create the button for shortcut mail
    def button_creation_shortcut_mail(self):
        button_mail = QPushButton('Accéder à votre boîte mail', self)
        button_mail.setGeometry(200, 400, 300, 50)
        button_mail.clicked.connect(self.mail_clicked)


    ## Open mail browser
    def mail_clicked(self):
        webbrowser.open(MAIL_URL)

    
    ## Create the button for shortcut taxes
    def button_creation_shortcut_taxes(self):
        button_mail = QPushButton('Accéder au service des impots', self)
        button_mail.setGeometry(200, 300, 300, 50)
        button_mail.clicked.connect(self.taxes_clicked)


    ## Open taxes browser
    def taxes_clicked(self):
        webbrowser.open(TAXES_URL)


    def display_wifi_available(self):
        # Using the check_output() for having the network term retrival
        devices = subprocess.check_output(['netsh','wlan','show','network'])
        
        # Decode it to strings
        devices = devices.decode('ascii')
        devices = devices.replace("\r","")
        
        # Displaying the information
        print(devices)


        ## Create the button for shortcut wifi
    def button_creation_shortcut_wifi(self):
        button_mail = QPushButton('Se connecter à la Wifi', self)
        button_mail.setGeometry(200, 100, 300, 50)
        button_mail.clicked.connect(self.wifi_clicked)

    def wifi_clicked(self):
        name_of_router = WIFI_ID
        name_of_router_bis = WIFI_ID_BIS
        if platform.system() == "Windows" :
            # connect to the given wifi network
            os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')
            os.system(f'''cmd /c "netsh wlan connect name={name_of_router_bis}"''')


        self.internet_clicked()




def main():
    app = QApplication([])
    window = Window()
    #if platform.system() == "Windows":
    #    window.display_wifi_available()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()
