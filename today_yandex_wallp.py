"""
New_Yandex_wallpepper_every_day 
ver 0.2
"""

import time, datetime, os, urllib.request, ctypes, shutil

#file name with current dir:
name_jpg = os.getcwd() + os.sep + 'tywall.jpg'
name_save = os.getcwd() + os.sep + time.strftime('%Y%m%d') + '.jpg'

#current date:
now_date = datetime.date.today() 

#variable for checking:
data=open("data.txt","r")
yday_date=data.read() 

def pars(name_arg):
    """Download pic from yandex.ru with required resolution"""
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [width, height] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    url = "https://yandex.ru/images/today?size=" + str(width) + "x" + str(height)
    img = urllib.request.urlopen(url).read()
    out = open(name_arg, "wb")
    out.write(img)
    out.close()


if str(now_date) > str(yday_date):
    pars(name_jpg)

    #set new desk wallpaper 
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, name_jpg, 0)

    #save changes
    yday_date = now_date
    data = open("data.txt","w")
    data.write(str(yday_date))
    data.close()
else:
    data.close()

#input("Looks good? (Y/N): ") # add machine learning

#saving:
def saving():
    """Save today wallpapper to current dir"""
    while True:
        print("Do you like today wallpapper? Save? (Y/N):")
        response = input().upper()  
        if response == "Y":
            print("Saved: {}".format(response))

            shutil.copyfile(name_jpg, name_save, follow_symlinks=True)
            
            print("Exit...")
            quit()
        elif response == "N":
            print("Ok, exit".format(response))
        else:
            print("Please reinsert: {}".format(response))
            print("   ")

saving()