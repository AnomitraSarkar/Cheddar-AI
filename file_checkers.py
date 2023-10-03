'''
INITIALIZER OF FILE AND DIRECTORY SYSTEM
'''
import algorithm as algo
import os, csv
from time import sleep
from tkinter import *
from PIL import Image, ImageTk
import random

# default directories
vars_dir = {
"name_woman" : "KIARA",
"name_man" : "KIRA",
"input_directory" : "INPUT",
"output_directory" : "OUTPUT",
"video_port_directory" : "VIDEO PORT",
"audio_inlet_directory" : "AUDIO_INLET",
"assest_directory" : "ASSEST",
"data_directory" : "DATA"}

# default profile filenmame = "{data_directory}/profiles.csv"
# default preloader filename is preloader.csv and cannot be changed
preload_file = "preloader.csv"

template_preloader_csv = [
["name_woman","KIARA"],
["name_man","KIRA"],
["input_directory","INPUT"],
["output_directory","OUTPUT"],
["video_port_directory","VIDEO_PORTS"],
["audio_inlet_directory","AUDIO_OUTLET"],
["assest_directory","ASSEST"],
["data_directory","DATA"],
]

template_profile_csv = [
    ["Names","Password","Call_list"],
    ["BOSS", "admin", "boss"]
]

person_name = "BOSS" 
person_pass = "BOSS" 
person_call_list = ["BOSS" ]

# Functionalities
def understand_preloader(filename):
    quote = algo.read_file(filename=filename)
    for i in quote:
        vars_dir[i[0]] = i[1]

def profile_setter(pswd,  pfile):
    pdat = algo.read_file(pfile)
    pdat = pdat[1:]
    for i in pdat:
        if i[1].lower() == pswd:
            global person_name, person_pass, person_call_list
            person_name = i[0]
            person_pass = i[1]
            person_call_list = i[2].split()
            return True
    return False

def readFakeTask():
    with open("ASSEST/fakelist.csv") as f:
        cmds = f.readlines()
    return cmds


def template_profile(fname):
    if os.path.isfile(fname):
        return 1
    else:
        algo.write_file(fname, template_profile_csv)
        return 0

def phrase_call(caller):
    return caller[random.randint(0,len(caller)-1)]

def create_default_preloader():
    if os.path.isfile(preload_file):
        return 1
    else:
        algo.write_file(preload_file, template_preloader_csv)
        return 0


def checkfordirectory():
    for i in vars_dir:
        if os.path.isdir(vars_dir[i]):
            continue
        else:
            os.system(f"mkdir {vars_dir[i]}")

def display_cheddar_image():
    img = Image.open("ASSEST/cheddar.jpg")
    x = img.size
    img = img.resize((x[0],x[1]))

    root = Tk()
    root.title("WELCOME TO CHEDDAR AI!")
    root.eval('tk::PlaceWindow . top')
    
    scwid = root.winfo_screenwidth()-x[0]
    schgt = root.winfo_screenheight()-x[1]
    root.geometry(f"{x[0]}x{x[1]}+{int(scwid/2)}+{int(schgt/2)}")
    testimg = ImageTk.PhotoImage(img)
    label = Label(image=testimg)
    label.pack()
    root.after(3000,lambda:root.destroy())
    root.mainloop()

if __name__ == "__main__":
    # create_default_preloader()
    # understand_preloader(preload_file)
    # profiles_file = f"{vars_dir['data_directory']}\profiles.csv"
    # checkfordirectory()
    # template_profile(profiles_file)
    # display_cheddar_image()
    # profile_setter(input("Password: "), 'DATA\profiles.csv')
    # print(person_name, person_pass, person_call_list)
    # call = phrase_call(person_call_list)
    # print("Hello", call)
    # x = readFakeTask()
    # for i in x:
    #     print(i)
    # declarecmds(readFakeTask())
    pass
    