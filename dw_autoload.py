"""
Daily Wallpapper from Bing.com
ver. 0.61 _ autoload module
Smirnov Alexey
https://github.com/samwl
"""

import sys, time, os, urllib.request, ctypes, json   

global name_jpg
name_jpg = os.getcwd() + os.sep + 'dw_temp.jpg'

def main_f():
    try_num = 180
    while try_num != 0:
        try:
            pars(name_jpg)
        except urllib.error.URLError:
            time.sleep(60)
            try_num -= 60
        else: 
            set_wallpapper()
            time.sleep(3)
            self_cleaning()
            sys.exit(1)
    sys.exit(1)

def pars(name_arg):
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

def set_wallpapper():
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, name_jpg, 0)

def self_cleaning():
    """Delete autoload app from startup dir"""
    list_d = os.listdir(os.getcwd())
    if 'dw_temp.jpg' in list_d:
        os.remove('dw_temp.jpg')

main_f()                   

if __name__ == "__main__":
    main_f()