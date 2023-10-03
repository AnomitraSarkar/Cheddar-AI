# ---------------------- START OF FILE ----------------------
  
# IMPORTS AND DEPENDENCIES

import pyttsx3 as tts
import pyautogui as pag
import csv
import speech_recognition as sr
import os
import time
import threading
import socket
import subprocess
from tabulate import tabulate as table_maker
from tkinter import filedialog
import file_checkers as fc
import matplotlib.pyplot as plot
import re

# GETTERS AND SETTERS 

def defaultSetters():
    pass

gendervar = 'woman'  # default sat to KIARA

speakerEngine = tts.init('sapi5')
r = sr.Recognizer()

# SPEAKER AND LISTENER FUNCTIONATIES

def speakCommand(silence, text):
    if "enable" in silence.lower():
        speakerEngine.say(text)
        speakerEngine.runAndWait()
    else:
        print(text)

def changeVoiceOfAI(stat):
    voice = speakerEngine.getProperty('voices')
    if stat == 'man':
        speakerEngine.setProperty('voice', voice[0].id)
        speakerEngine.say("Voice changed to KIRA")
        speakerEngine.runAndWait()
        # AI becomes KIRA
    else:
        speakerEngine.setProperty('voice', voice[1].id)
        speakerEngine.say("Voice changed to KIARA")
        speakerEngine.runAndWait()
        # AI becomes KIARA


def listenCommandCmd(silence=None):
    cmd = input("Enter your command boy: ")
    speakCommand(silence, "Enter your command boy: ")
    return cmd.lower()


def listenCommandAudio():
    # r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening my Boi...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"My Boi said: {query}\n")
    except Exception as e:
        print(e, "Say that again please...")
        return "None"
    return query

# FUNCTIONALITIES 

def networkCheck(silence):
    net = socket.gethostbyname(socket.gethostname())
    stat = not net == '127.0.0.1'
    if stat:
        speakCommand(silence, "Connected to a network")

    else:
        speakCommand(silence, "Not connected to any intermidiate network")
    return stat



def read_file(filename):
    preloaderdata = []
    with open(filename, 'r') as f:
        csv_reader = csv.reader(f)
        for i in csv_reader:
            preloaderdata.append(i)
    return preloaderdata


def password_inlet():
    pswd = pag.password("Enter your Registered password")
    return pswd

def clearConsole(silence=None):
    speakCommand(silence, "Clearing the console")
    os.system("cls")


def customCmdCommands(silence):
    os.system(listenCommandCmd(silence))


def openNewCmd(silence, call="Boss"):
    speakCommand(silence, f"Opening new command prompt window {call} ")
    os.system("start")


def startMusic(silence, call="boss"):
    speakCommand(silence, f"Playing music from your music folder {call}")
    # deviate file name according to asset input or data input
    t = threading.Thread(target=dirprep, args=("ASSEST\music.bat",))
    t.start()
    t.join()

def listavailablenetworks(silence, connectstate=True, call='boss', index=1):
    command = "netsh wlan show networks".split()
    if connectstate == True:
        net = subprocess.check_output(command)
        net = net.decode('ascii')
        net = net.replace("\r", "")
        netprep = net.split("\n")
        netproc = []
        for i in netprep:
            if "ssid" in i.lower():
                netproc.append(i.strip())
        for i in range(0, len(netproc)):
            netproc[i] = netproc[i].replace(":", "<~>", 1)
            netproc[i] = netproc[i].split("<~>")
            netproc[i][0], netproc[i][1] = netproc[i][0].strip(
            ), netproc[i][1].strip()
            netproc[i][0] = netproc[i][0].replace('SSID ', '')
        speakCommand(silence, "wifi list obtained")
        print(table_maker(netproc, ['SSID', 'WI-FI NAME'], "fancy_grid"))
        for i in netproc:
            for j in i:
                speakCommand(silence, j)
        return netproc
    else:
        speakCommand(silence, "Wifi is off, no available networks")
        return None

def exitConsole(silence, command=None, call="Boss"):
    if command == None:
        speakCommand(silence, f"Exiting the console {call}")
        # os.system("exit")
        print("\n(------------------------------------FLUFFY BOY SAYS BYE------------------------------------)\n")
        exit()
    elif command == "direct shutdown":
        os.system("shutdown -s -t 10")
        speakCommand(silence, "Shuting System Down in 10 seconds")
        clearConsole()
        exitConsole(silence)
        speakCommand(silence, "See you later, bye")
    elif command == "direct restart":
        os.system("shutdown -r -t 10")
        speakCommand(silence, "Restarting System in 10 seconds")
        clearConsole(silence)
        exitConsole(silence)
        speakCommand(silence, "See you later, bye")

def check_input_directory(silence, directory="INPUT"):
    inputlist = os.listdir(directory)
    if inputlist == []:
        return False, False, False
    else:
        filelist = [f for f in inputlist if os.path.isfile(directory+"/"+f)]
        dirlist = [d for d in inputlist if os.path.isdir(directory+"/"+d)]
        speakCommand(
            silence, f"{len(inputlist)} items found in input directory")
        return inputlist, filelist, dirlist


def empty_directory(silence, directory):
    x, y, z = check_input_directory(silence, directory)
    if x:
        del x
        for i in y:
            # print(f"del {directory}/{i}")
            os.remove(f"{directory}/{i}")
        for j in z:
            os.rmdir(f"{directory}/{j}")
        speakCommand(silence, f"{directory} was emptied")

    else:
        speakCommand(silence, f"{directory} is already empty")


def dumpInOutput(directory, filename):
    pass


def write_file(filename, content):
    with open(filename, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(content)


def dirprep(filename):
    os.system(f"start {filename}")  # redundant functions dirprep and netprep


def netprep(filename):
    os.system(f"start {filename}")


def perpare_laptop(silence, filename1, filename2, call):
    speakCommand(
        silence, f"Preparing your laptop for work {call}, creating routine threads")
    t1 = threading.Thread(target=dirprep, args=(filename1,))
    t2 = threading.Thread(target=netprep, args=(filename2,))
    speakCommand(silence, "going through, the file system")
    t1.start()
    speakCommand(
        silence, "checking active network protocols, for foreign and internal activities.")
    t2.start()
    t1.join()
    t2.join()
    time.sleep(5)

def openparakeet(silence, call):
    speakCommand(silence, f"Opening New Parakeet Note {call}")
    os.system('ASSEST\parakeet.bat')

def openvscode(silence, mode=1):
    if mode == 1:  # previous session
        os.system("code -r")
        dname = "previous session"
    elif mode == 2:
        os.system("code -n")
        dname = "new session"
    elif mode == 3:
        dname = search_directory()
        os.system(f'code "{dname}"') # error
    else:
        os.system("code")
        dname = "general session"
    speakCommand(silence, f"opening visual studio code in {dname}")

def chrome_functions(silence, call, weblink = "", imod = False, browser = "chrome"):
    if imod == False:
        os.system(f"start {browser} {weblink}")
        speakCommand(silence, f"opening {weblink} in chrome {call}")
    elif imod == True:
        os.system(f"start {browser} /incognito {weblink}")
        speakCommand(silence, f"opening {weblink} in chrome incognito mode {call}")
    elif imod == "restore":
        os.system(F"start {browser} /restore-last-session")
        speakCommand(silence, f"restoring last chrome session {call}")

def spotify_function():
    os.system(r'start ASSEST\spotify.bat')
    
def whatsapp_function():
    os.system(r'start ASSEST\whatsappopener.bat')

def youtube_function(silence,call, str = "", browser = "brave"):
    if str != "":
        str= str.replace(" ", "+")
        os.system(f"start {browser} https://www.youtube.com/results?search_query={str}")
    else:
        os.system(f"start {browser} youtube.com")
    speakCommand(silence, f"opening youtube in {browser} {call}")

def fakeitcommand(ls, silence):
    speakCommand(silence, "Running file and required tasks in the background...")
    for i in ls:
        os.system(f'{i}')

def ytprocessor(raw):
    raw = raw.strip()
    raw = raw.replace("youtube", "",1)
    raw = raw.replace("yt", "",1)
    raw = raw.replace("open", "", 1)
    raw = raw.replace("play", "",1)
    return raw.strip()

def plotter():
    pass

def search_directory():
    try:
        dirname = filedialog.askdirectory(
            initialdir="C:/Users/91724/OneDrive/Desktop", title="SELECT DIRECTORY")
    except:
        dirname = "C:/Users/91724/OneDrive/Desktop"
    finally:
        return dirname

def webproc(raw):
    result = re.findall("[a-zA-z]+.\.com", raw)
    if result == []:
        return ""
    else:
        return result[0]

    
    
# EXPORT FUNCTION OF COMMANDS, COMBINATORICS CALL

# addition of callin functions for no error logs and catastrophic failure
def commands(silence, call, code=0, weblink=""):
    print("\n")
    if code == 0:  # for exiting the code
        exitConsole(silence, call=call)
    elif code == 1:  # for clearing the code
        clearConsole(silence)
    elif code == 2:  # for open thread fir music
        startMusic(silence, call)
    elif code == 3:  # direct shutdown
        exitConsole(silence, "direct shutdown")
    elif code == 4:  # direct restart
        exitConsole(silence, "direct restart")
    elif code == 5:  # prepare laptop
        perpare_laptop(silence, "ASSEST\prepare1.bat",
                       "ASSEST\prepare2.bat", call)
    elif code == 6:  # opening new cmd prompt
        openNewCmd(silence, call)
    elif code == 7:
        listavailablenetworks(silence, networkCheck('disabled'), call)
    elif code == 8:
        openvscode(silence)
    elif code == 9:
        openvscode(silence, 2)
    elif code == 10:
        openvscode(silence, 3)
    elif code == 11:
        openvscode(silence, 4)
    elif code == 12:
        chrome_functions(silence, call, weblink,False)
    elif code == 13:
        chrome_functions(silence, call, weblink, True)
    elif code == 14:
        chrome_functions(silence, call,"", "restore")
    elif code == 15:
        spotify_function()
        speakCommand(silence, f"firing up spotify {call}")
    elif code == 16:
        whatsapp_function()
        speakCommand(silence, f"starting up whatsapp {call}")
    elif code == 17:
        chrome_functions(silence, call, weblink,False, browser = "brave")
    elif code == 18:
        chrome_functions(silence, call, weblink, True, browser = "brave")
    elif code == 19:
        chrome_functions(silence, call,"", "restore", browser = "brave")
    elif code == 20:
        chrome_functions(silence, call, weblink,False, browser = "msedge")
    elif code == 21:
        chrome_functions(silence, call, weblink, True, browser = "msedge")
    elif code == 22:
        chrome_functions(silence, call,"", "restore", browser = "msedge")
    elif code == 24:
        youtube_function(silence, call, weblink)        
    elif code == 25:
        youtube_function(silence, call,weblink, "chrome")     
    elif code == 26:
        fakeitcommand(fc.readFakeTask(), silence)   
    elif code == 27:
        openparakeet(silence,call)

# MODULE MAIN FILE RUNNING INSTANCE

if __name__ == "__main__":
    speakmode = 'enabled'
    # openvscode(speakmode, 3)
    # spotify_function(speakmode)
    # commands(speakmode,'sir',24,'chikni chameli')
    print(ytprocessor("play yt 3js tutorial"))
    # print(webproc("open chrome in geeksforgeeks.com "))
    
# EXTRA COMMANDS FOR FUTURE PURPOSE

    '''
    list wifi

    # importing the subprocess module
import subprocess

# using the check_output() for having the network term retrieval
devices = subprocess.check_output(['netsh','wlan','show','network'])  # change this to get the necessary output and manipulate it

# decode it to strings
devices = devices.decode('ascii')
devices= devices.replace("\r","")

# displaying the information
print(devices)
    
    '''

    '''
    turning on wifi
    cmd : admin run
    cmd : netsh interface set interface "Wi-Fi" enable/disable
    
    '''

    '''
    connecting to wifi
    cmd : admin run
    cmd : netsh wlan connect name = "VITC-HOS2-4"

    '''

'''
whatsapp file location
"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2323.2.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
docstring required


YOUTUBE SEARCH QUERY
https://www.youtube.com/results?search_query=hello+bois
'''
# https://youtu.be/q7qdpyjHyNk

# ----------------------- END OF FILE -----------------------  