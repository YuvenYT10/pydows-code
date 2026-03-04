import sys
import time
import os
import platform
import math
users = []
def t(text, speed=0.05):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch in ",.!?":
            time.sleep(speed * 6)
        else:
            time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()
def c():
    if os.name == "nt":
        os.system("cls")
        time.sleep(0.5)
    else:
        os.system("clear")
        time.sleep(0.5)
def instal():
    t("install pydows 10")
    t("1. install")    
    t("2. exit")
    insta = input(": ")
    if insta == "install":
        install()
    elif insta == "exit":
        exit()
    else:
        t("invalid choice")
        c()
        return
def install():
    c()
    t("--- pydows 10 Setup ---")
    t("Starting Windows Setup...")
    t("Checking system requirements...")
    t("Copying pydows files...")
    t("Installing features...")
    t("Installing updates...")
    t("Finishing up...")
    t("Restarting...")
    c()
    t("Preparing pydows...")
    t("Don't turn off your PC.")
    c()
    t("Hi.")
    t("We're getting things ready for you.")
    t("This might take a few minutes.")
    time.sleep(1)
    t("All set!")
    t("Welcome to pydows 10.")
    username = input("username: ")
    password = input("password: ")
    users.append({username: password})
    lock()
def lock():
    while True:
        c()
        t("lock screen")
        user = input("input your username: ")
        passes = input("input your password: ")
        if {user: passes} in users:
            t("correct password!")
            home()
        else:                
            t("incorrect username or password")
def home():
    t("pydows 10 home page")
    t("1. apps")
    t("2. sign out")
    t("3. shut down")
    homes = input(": ")
    if homes == "apps":
        apps()
    elif homes in ["sign out","sign"]:
        lock()
    elif homes in ["shut down","shut"]:
        t("shuttimg down...")
        exit()
def apps():
    c()
    t("apps")
    t("1. Google")
    t("2. Minecraft")
    t("3. PyDroid 3")
    t("4. calculator")
    t("5. Phone Details")
    app = input("apps: ")
    if app == "google":
        google()
    elif app == "minecraft":
        mine()
    elif app in ["pydroid","python","pydroid 3"]:
        pydroid()
    elif app in ["calculator","calc"]:
        calc()
    elif app in ["phone details","phone","details"]:
        Details()
    else:
        t("invalid choice")
        apps()
def google():
    c()
    t("google")
    t("1. Youtube")
    t("2. eaglercraft")
    search = input(": ")
    if search in ["youtube","Youtube"]:
        t("no internet connect")
    elif search == "eaglercraft":
        eaglerhome()
def mine():
    c()
    t("no 3D generator detected ")
    t("please add a 3D terrain generator in this to continue into minecraft")
    apps()
def pydroid():
    c()
    code = input(">>> ")
    try:
        if code in ["exit","quit","close"]:
            apps()
        elif code == "":
            pydroid()
        else:
            exec(code)
            pydroid()
    except Exception as k:
        t(f"Error: {k}")
        pydroid()
def calc():
    c()
    while True:
        try:
            a = int(input("1st number:"))  
        except ValueError as e:
            t(f"ValueError: {e}")
            continue  # go back to the start if invalid input

        op = input("operation: ")  

        if op in ["exit","quit"]:  
            apps()  
        elif str(a) in ["exit","quit"]:  # make sure to compare a as string
            apps()  
        elif op == "sqrt":  
            try:  
                result = math.sqrt(a)  
                t(f"{a}√ = {result}")  
            except ValueError as v:  
                t(f"ValueError: {v}")  
        else:
            try:
                b = int(input("2nd operation"))
            except ValueError as v:
                t(f"ValueError: {v}")
                continue  
            if op == "+":  
                t(f"{a}+{b}={a+b}")  
            elif op == "-":  
                t(f"{a}-{b}={a-b}")  
            elif op == "*":  
                t(f"{a}*{b}={a*b}")  
            elif op == "/":  
                try:  
                    t(f"{a}/{b}={a/b}")  
                except ValueError as e:  
                    t(f"ValueError {e}")  
                except ZeroDivisionError as e:  
                    t(f"ZeroDivisionError: {e}")
def Details():
    c()
    t("Phone Details")
    os = platform.system()
    architechure = platform.architecture()
    machine = platform.machine()
    release = platform.release()
    t(f"architecture: {architechure}")
    t(f"machine: {machine}")
    t(f"release: {release}")
    t(f"kernal: {os}")
    apps()
def eaglerhome():
    t("singleplayer")
    t("multiplayer")
    t("exit")
    eaglercraft = input("option: ")
    if eaglercraft in ["singleplayer","single"]:
        t("work in progress")
    elif eaglercraft in ["multiplayer","multi","mtiuser"]:
        t("servers:")
        t("ArchMC")
        t("add server")
        server = input("server: ")
        if server in ["ArchMC","archmc"]:
            t("connecting...")
            t("handshake failed")
            eaglerhome()
        elif server in ["add server","add","mew server"]:
            SSID = input("Server Name: ")
            IP = input("Server IP Adress: ")
            t("couldnt find server")
            eaglerhome()
        else:
            t("invalid choice")
            eaglerhome()
    elif eaglercraft in ["exit","quit"]:
        apps()
    else:
        t("invalid choice")
        eaglerhome()
apps()