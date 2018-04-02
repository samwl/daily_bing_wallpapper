"""
Daily Wallpapper from Bing.com
ver. 0.51

Smirnov Alexey
https://github.com/samwl
"""

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QSplashScreen
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, Qt
import sys, time, datetime, os, urllib.request, ctypes, shutil, json   
             
             
class TYW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # button 1
        self.button1 = QPushButton("Update", self)
        self.button1.clicked.connect(self.main_f)
        self.button1.move(10, 45)
        self.button1.setStyleSheet("""
                    QPushButton:hover { color: #333;
                        border: 1px solid #7E3FF0;
                        border-radius: 0px;
                        padding: 0px;
                        background: #fff;
                        min-width: 80px; }
                    QPushButton:!hover {;
                        border: 1px solid #555;
                        border-radius: 0px;
                        padding: 0px;
                        background: rgb(253, 232, 89);     
                        min-width: 80px;}
                    QPushButton:pressed {; 
                        border: 1px solid #555;
                        border-radius: 0px;
                        padding: 0px;
                        background: rgb(254, 251, 208);
                        min-width: 80px;}   
                                    """)
        # button 2
        self.button2 = QPushButton("Save", self)
        self.button2.clicked.connect(self.saving)
        self.button2.move(10, 45)
        self.button2.setStyleSheet("""
                    QPushButton:hover { color: #333;
                        border: 1px solid #7E3FF0;
                        border-radius: 0px;
                        padding: 0px;
                        background: #fff;
                        min-width: 80px; }
                    QPushButton:!hover {;
                        border: 1px solid #555;
                        border-radius: 0px;
                        padding: 0px;
                        background: rgb(253, 232, 89);
                        min-width: 80px;}
                    QPushButton:pressed {; 
                        border: 1px solid #555;
                        border-radius: 0px;
                        padding: 0px;
                        background: rgb(254, 251, 208);
                        min-width: 80px;} 
                                    """)
        self.button2.hide()

        # text label
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 200, 30))

        # window_form
        self.setGeometry(300, 300, 230, 93)
        self.setFixedSize(230, 93)
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                            "font: 9pt \"Segoe UI\";")
        self.setWindowTitle('Daily Wallpapper')
        self.setWindowIcon(QIcon('icoo.ico'))
        self.statusBar().showMessage('ver. 0.51')
        self.statusBar().setStyleSheet("font: 6pt \"Segoe UI\";\n")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.initial_message()
        self.show()

    def show_save_button(self):
        self.button2.show()

    def initial_message(self):
        # first message №1
        self.label.setText("Hello! Press 'Update' to get \ntoday wallpapper")

    def buttonClicked1(self):
        tyw.main_f()
        sender = self.sender()
        
    def buttonClicked2(self):
        tyw.saving()
        sender = self.sender()

    def status_ex(self):
        #autoexit func (timer on 5 sec):
        self.label.setText("Exit after 5 seconds")
        QTimer.singleShot(2000, self.quit_e)

    def quit_e(self):
        app.quit()

    def pars(self, name_arg):
        """Download image from bing.com"""
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        [width, height] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
        js = urllib.request.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')
        js_obj = json.load(js)
        url = 'http://www.bing.com' + js_obj['images'][0]['url']
        js.close()
        img = urllib.request.urlopen(url).read()
        out = open(name_arg, "wb")
        out.write(img)
        out.close()

    def saving(self):
        """Save today wallpapper to current dir"""
        list_d = os.listdir()
        a_folder = "saved_wallpapper"
        if a_folder in list_d:
            shutil.copyfile(name_jpg, name_save, follow_symlinks=True)
        else:
            path = os.getcwd() + os.sep + "/saved_wallpapper"
            os.mkdir(path)
            shutil.copyfile(name_jpg, name_save, follow_symlinks=True)
        self.label.setText("Saved")
        QTimer.singleShot(1000, self.status_ex) 

    def set_wallpapper(self):
        """set new desk wallpaper"""
        SPI_SETDESKWALLPAPER = 20 
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, name_jpg, 0)

    def save_data(self):
        """Save log"""
        y_date = datetime.date.today() 
        data = open("data.txt","w")
        data.write(str(y_date))
        data.close()

    #file name with current dir:
    global name_jpg
    name_jpg = os.getcwd() + os.sep + 'tywall.jpg'
    global name_save
    name_save = os.getcwd() + os.sep + '/saved_wallpapper/' + time.strftime('%d_%h_%Y') + '.jpg'

    def main_f(self): 
        with open('data.txt') as data_log:
            yday_date = data_log.readline()
        #checking
            if str(datetime.date.today()) > str(yday_date):
                self.pars(name_jpg)
                self.set_wallpapper()
                self.save_data()
                self.show_save_button()
                self.label.setText("Updated")
                self.button1.hide()
                QTimer.singleShot(1500, self.message_s)
            else:
                self.label.setText("Installed the latest wallpapers")
                QTimer.singleShot(3000, self.status_ex)

    def message_s(self):
        self.label.setText("Do you like it? Save?")
                   

if __name__ == "__main__":
    app = QApplication([])
    start = time.time() 
    load_img = os.getcwd() + os.sep + 'load.png' 
    splash = QSplashScreen(QPixmap(load_img))
    splash.show()
    while time.time() - start < 1:
        time.sleep(0.2)
        app.processEvents()
    ex = TYW()
    splash.finish(ex)
    ex.show()
    app.exec_()