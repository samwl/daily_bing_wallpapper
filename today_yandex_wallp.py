"""
New_Yandex_wallpepper_every_day 
ver 0.1
"""

import datetime, os, urllib.request, ctypes

#file name with current dir:
name_jpg = os.getcwd() + os.sep + 'tywall.jpg'

#current date:
now_date = datetime.date.today() 

#variable for checking:
data=open("data.txt","r")
yday_date=data.read() 

if str(now_date) > str(yday_date):
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [width, height] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    url = "https://yandex.ru/images/today?size=" + str(width) + "x" + str(height)
    img = urllib.request.urlopen(url).read()
    out = open(name_jpg, "wb")
    out.write(img)
    out.close()

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
