from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import requests
import json
import ctypes

app = QApplication([])
app.setQuitOnLastWindowClosed(False)


ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)



url = "https://api.binance.com/api/v3/ticker/price?symbol="
  
def crypto_price(test):
    data = requests.get(url + test)  
    data = data.json()
    return(data['price'])





def BTCAUD():
    tray.showMessage("BTCAUD Price", str(crypto_price("BTCAUD")), QIcon("btc.png"), 10000)
    #change the notification icon 
    
def ETHAUD():
    tray.showMessage("ETHAUD Price", str(crypto_price("ETHAUD")), QIcon("eth.png"), 10000)
    #change the notification icon     
 
def DOGEAUD():
    tray.showMessage("DOGEAUD Price", str(crypto_price("DOGEAUD")), QIcon("doge.png"), 10000)
    #change the notification icon        

def ADAAUD():
    tray.showMessage("ADAAUD Price", str(crypto_price("ADAAUD")), QIcon("ada.png"), 10000)
    #change the notification icon

def BNBAUD():
    tray.showMessage("BNBAUD Price", str(crypto_price("BNBAUD")), QIcon("bnb.png"), 10000)
    #change the notification icon   


icon = QIcon("btc.png")

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Creating the options
menu = QMenu()
option1 =QAction("BTCAUD")
option1.triggered.connect(BTCAUD)
option2 = QAction("ETHAUD")
option2.triggered.connect(ETHAUD)
option3 = QAction("DOGEAUD")
option3.triggered.connect(DOGEAUD)
option4 = QAction("ADAAUD")
option4.triggered.connect(ADAAUD)
option5 = QAction("BNBAUD")
option5.triggered.connect(BNBAUD)




menu.addAction(option1)
menu.addAction(option2)
menu.addAction(option3)
menu.addAction(option4)
menu.addAction(option5)




# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Adding options to the System Tray
tray.setContextMenu(menu)

app.exec_()