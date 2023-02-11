import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from random import *
class LoginForm(QDialog):
    def __init__(self, parent=None):
        super(LoginForm, self).__init__(parent)
        loadUi("Brute_Force_Attack.ui",self)  
        self.Attack.clicked.connect(self.Findpass)
        self.match.setHidden(True)

    def Findpass(self):
        password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
                    'w', 'x', 'y', 'z',0,1,2,3,4,5,6,7,8,9] #A-Z !@#$%^&*
        guess=""
        store=self.Input.text()        
        while (guess != store):
            guess = ""
            for letter in range(len(store)):
                guess_letter = password[randint(0, 25)]
                guess = str(guess_letter) + str(guess)
            if(guess != store):
                self.output.insertPlainText(guess)  #Trying password more time
                self.output.insertPlainText("\n")
            elif(guess==guess):
                self.output.setStyleSheet("color:red;background-color:none;")
                FndPass=self.match.setText(guess)
                self.output.insertPlainText(FndPass) #Find password here. 
                self.match.setHidden(False)

               
app = QApplication(sys.argv)
form = LoginForm()
form.show()
app.exec_()









#Brute_Force_Attack.ui Attack
