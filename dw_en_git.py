"""
Daily Wallpapper from Bing.com
ver. 0.60

Smirnov Alexey
https://github.com/samwl
"""

from PyQt5.QtWidgets import QMainWindow, QWidget,QFileDialog, QApplication, QPushButton, QLabel, QSplashScreen, QCheckBox, QToolTip
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, Qt
import sys, time, datetime, os, urllib.request, ctypes, shutil, json, getpass, pickle   
                    
class TYW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    # Global vars:
    global data_db
    data_db = os.getcwd() + os.sep + 'db.dat'
    global db
    db = open(data_db, 'rb')
    global data
    data = pickle.load(db)
    global save_path
    save_path = os.getcwd() + os.sep + 'saved_wallpapper/'
    global default_path
    default_path = data[1]
    global user_name
    user_name = getpass.getuser()
    global startup_dir
    startup_dir = "C:/Users/" + user_name  + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"
    global al_path
    al_path = os.getcwd() + os.sep + 'dw_autoload.exe'
    global al_exe
    al_exe = 'dw_autoload.exe'
    global name_jpg
    name_jpg = os.getcwd() + os.sep + 'dw.jpg'
    global name_save
    name_save = os.getcwd() + os.sep + '/saved_wallpapper/' + time.strftime('%d_%h_%Y') + '.jpg'
    

    def initUI(self):
        # button Update
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
        # Checkbox autoload                            
        self.cb = QCheckBox('Auto-update', self)
        self.cb.move(120, 37)
        self.cb.stateChanged.connect(self.autoload)
        # button Save
        self.button2 = QPushButton("Save", self)
        self.button2.setToolTip('Save in: ' + save_path)
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
                    QToolTip { 
                        color: #333;
                        border: 1px solid #7E3FF0;
                        border-radius: 0px;
                        padding: 0px;
                        font: 9pt \"Segoe UI\";
                        background: #fff;
                        min-width: 60px; }                
                                    """)
        self.button2.hide()
        # button First 'No' 
        self.button31 = QPushButton("No", self)
        self.button31.clicked.connect(self.choice_s)
        self.button31.move(115, 45)
        self.button31.setStyleSheet("""
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
        self.button31.hide()
        # button Second 'No'
        self.button3 = QPushButton("No", self)
        self.button3.clicked.connect(self.status_ex)
        self.button3.move(115, 45)
        self.button3.setStyleSheet("""
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
        self.button3.hide()
        # button - Return the default wallpaper
        self.button4 = QPushButton("Return", self)
        self.button4.clicked.connect(self.return_def_wall)
        self.button4.setToolTip(default_path)
        self.button4.move(10, 45)
        self.button4.setStyleSheet("""
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
                    QToolTip { 
                        color: #333;
                        border: 1px solid #7E3FF0;
                        border-radius: 0px;
                        padding: 0px;
                        font: 9pt \"Segoe UI\";
                        background: #fff;
                        min-width: 60px;}    
                                    """)
        self.button4.hide()
        #button5 - Set the default wallpaper
        self.button5 = QPushButton("Set default", self)
        self.button5.clicked.connect(self.set_default_path)
        self.button5.setToolTip('You can change the default wallpapper')
        self.button5.setGeometry(QtCore.QRect(120, 60, 30, 15))
        self.button5.setStyleSheet("""
                    QPushButton:hover { color: #333;
                        border: 1px solid #7E3FF0;
                        border-radius: 0px;
                        padding: 0px;
                        font: 9pt \"Segoe UI\";
                        background: #fff;
                        min-width: 80px; }
                    QPushButton:!hover {color: rgb(180, 180, 180);
                        border: 1px solid #555;
                        border-radius: 0px;
                        padding: 0px;
                        font: 9pt \"Segoe UI\";
                        background: #fff;
                        min-width: 80px;}
                    QPushButton:pressed {; 
                        border: 1px solid #555;
                        border-radius: 0px;
                        padding: 0px;
                        font: 9pt \"Segoe UI\";
                        background: rgb(254, 251, 208);
                        min-width: 80px;} 
                    QToolTip { 
                        color: #333;
                        border: 1px solid #7E3FF0;
                        border-radius: 0px;
                        padding: 0px;
                        font: 9pt \"Segoe UI\";
                        background: #fff;
                        min-width: 65px;}    
                                    """)
        # Text output
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 5, 200, 35))
        # Window_form
        self.setGeometry(300, 300, 230, 93)
        self.setFixedSize(230, 93)
        self.setStyleSheet("""background-color: rgb(255, 255, 255);
                            font: 10pt \"Segoe UI\";""")
        self.setWindowTitle('Daily Wallpapper')
        self.setWindowIcon(QIcon('icoo.ico'))
        self.statusBar().showMessage('ver. 0.60')
        self.statusBar().setStyleSheet("font: 6pt \"Segoe UI\";\n")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.initial_message()
        self.show()

    def autoload(self, state):
        """Checkbox func"""
        if state == Qt.Checked:
            self.autoload_on()
        else:
            self.autoload_off()

    def autoload_off(self):
        """Delete autoload app from startup dir"""
        list_d = os.listdir(startup_dir)
        if al_exe in list_d:
            os.remove(startup_dir + al_exe)
        self.label.setText('Autoload - OFF')

    def autoload_on(self):
        """Copy autoload app to startup dir"""
        list_d = os.listdir(startup_dir)
        if al_exe not in list_d:
            shutil.copyfile(al_path, startup_dir + al_exe, follow_symlinks=True)
        self.label.setText('Autoload - ON')

    def initial_message(self):
        self.label.setText("Hello! Press 'Update' to get \ntoday wallpapper")

    def status_ex(self):
        """Auto exit"""
        self.label.setText("Exit after a few seconds")
        QTimer.singleShot(2000, self.quit_e)

    def quit_e(self):
        app.quit()

    def pars(self, name_arg):
        """Download image from bing.com"""
        #user32 = ctypes.windll.user32
        #user32.SetProcessDPIAware()
        #[width, height] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] - choice requred resolution not work now
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
        """Set new desk wallpaper"""
        SPI_SETDESKWALLPAPER = 20 
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, name_jpg, 0)

    def save_data(self):
        """Save current change"""
        data[0] = str(datetime.date.today()) 
        self.write_db(data)

    def read_db(self):
        """Read save data from db.DAT"""
        try:
            db = open(data_db, 'rb')
        except FileNotFoundError:
            self.open_error_message()
        else:
            data = pickle.load(db)
            return data

    def write_db(self, data):
        """Save updated data to db.DAT"""
        try:
            db = open(data_db, 'wb')
        except FileNotFoundError:
            self.open_error_message()
        else:
            pickle.dump(data, db)
            db.close()

    def main_f(self):
        """Main update func"""
        yday_date = data[0]
        #checking
        if str(datetime.date.today()) > str(yday_date):
            try:
                self.pars(name_jpg)
            except urllib.error.URLError:
                self.connection_error_message()
                QTimer.singleShot(2000, self.status_ex)
            else: 
                self.set_wallpapper()
                self.save_data()
                self.button2.show()
                self.button31.show()
                self.label.setText("Updated")
                self.button1.hide()
                self.button5.hide()
                self.cb.hide()
                QTimer.singleShot(1500, self.message_s)
        else:
            self.label.setText("Installed the latest wallpapers")
            self.button1.hide()
            self.button5.hide()
            self.cb.hide()
            self.choice_s()
                
    def open_error_message(self):
        self.label.setText("Please check - db.DAT")
        QTimer.singleShot(1000, self.status_ex)

    def connection_error_message(self):
        self.label.setText("Сheck internet connection")
        QTimer.singleShot(1000, self.status_ex)

    def message_s(self):
        self.label.setText("Do you like it? Save?")

    def message_c(self):
        self.label.setText("Return the default wallpaper?")

    def choice_s(self):
        """Return choice"""
        self.button3.show()
        self.button4.show()
        QTimer.singleShot(1300, self.message_c)
        
    def return_def_wall(self):
        """Return to default wall"""
        data = self.read_db()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, data[1], 0)
        data[0] = '2010-00-00' 
        self.write_db(data)
        QTimer.singleShot(1000, self.status_ex)

    def set_default_path(self):
        """Set path to default wallpapper"""
        fname = QFileDialog.getOpenFileName(self, 'Select default wallpaper', '/home')[0]
        dir_name = os.path.dirname(fname)
        file_name = os.path.basename(fname)
        data = self.read_db()
        data[1] = dir_name + '/' + file_name
        self.write_db(data)
                  
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
