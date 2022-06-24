from tkinter import *
import time
import threading
import requests.exceptions
from pynput.keyboard import Listener, KeyCode
import os
from colorama import *
import platform
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

win = Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("Calcolatrice")


def clicker():
    os.system("cls")
    os.system("title ClickAx")
    print(f"""\r{Fore.RED}     
                              ▄████▄   ██▓     ██▓  ▄████▄  ██ ▄█▀ ▄▄▄     ▒██   ██▒
                            ▒██▀ ▀█  ▓██▒   ▒▓██▒ ▒██▀ ▀█  ██▄█▒ ▒████▄   ▒▒ █ █ ▒░
                            ▒▓█    ▄ ▒██░   ▒▒██▒ ▒▓█    ▄▓███▄░ ▒██  ▀█▄ ░░  █   ░
                            ▒▒▓▓▄ ▄██ ▒██░   ░░██░▒▒▓▓▄ ▄██▓██ █▄ ░██▄▄▄▄██ ░ █ █ ▒ 
                            ░▒ ▓███▀ ▒░██████░░██░░▒ ▓███▀ ▒██▒ █▄▒▓█   ▓██▒██▒ ▒██▒
                            ░░ ░▒ ▒  ░░ ▒░▓   ░▓  ░░ ░▒ ▒  ▒ ▒▒ ▓▒░▒▒   ▓▒█▒▒ ░ ░▓ ░
                               ░  ▒  ░░ ░ ▒  ░ ▒ ░   ░  ▒  ░ ░▒ ▒░░ ░   ▒▒ ░░   ░▒ ░
                            ░          ░ ░  ░ ▒ ░ ░       ░ ░░ ░   ░   ▒   ░    ░  
                            ░ ░     ░    ░    ░   ░ ░     ░  ░         ░   ░    ░    {Fore.BLUE} V 1.1
                                                                                                {Fore.CYAN + Style.BRIGHT} By akarta#8195 
                                                                                                {Fore.YELLOW + Style.BRIGHT} Per supporto entra qui › {Fore.BLUE}https://dsc.gg/clickax""")

    ora = datetime.now()
    str_current_datetime = str(ora)
    d = input(f"{Fore.CYAN}Seleziona i CPS, da 10 a 20:{Fore.YELLOW} ")
    my_os = platform.platform()

    '''
    0.09 10
    0.08 11
    0.07 13
    0.06 14
    0.055 15
    0.049 16
    0.047 17
    0.0445 18
    0.0442 19
    0.044 20
    '''

    if d == "10":
        delay = float(0.09)
    elif d == "11":
        delay = 0.08
    elif d == "12":
        delay = 0.07
    elif d == "13":
        delay = 0.07
    elif d == "14":
        delay = 0.06
    elif d == "15":
        delay = 0.055
    elif d == "16":
        delay = 0.049
    elif d == "17":
        delay = 0.047
    elif d == "18":
        delay = 0.0445
    elif d == "19":
        delay = 0.0442
    elif d == "20":
        delay = 0.044
    else:
        print(f"\n       {Fore.RED}Per favore, seleziona dei cps giusti!")
        back2()

    t = input(f"{Fore.CYAN}Tasto destro o sinistro:{Fore.YELLOW} ")
    from pynput.mouse import Button, Controller
    if t == "d":
        button = Button.right
    elif t == "s":
        button = Button.left
    else:
        print(f"\n       {Fore.RED}Per favore, seleziona il tasto corretto!")
        back2()
    s = input(f"{Fore.CYAN}Tasto per attivarlo/disattivarlo:{Fore.YELLOW} ")
    e = input(f"{Fore.CYAN}Tasto per spegnerlo:{Fore.YELLOW} ")

    try:
        webhook = DiscordWebhook(
            url='https://discord.com/api/webhooks/980805288221351986/sDKZFNDCgQniKbNlqy-9e7vS1AnXR1Yf8xWtb3XG2cqhsusWmMusVz4cAylnEGbrwnB8',
            username="ClickAx  Logs")

        embed = DiscordEmbed(title='Logs', color='5b92e5')
        embed.set_author(name='ClickAx', url='https://solo.to/serra', icon_url='https://i.imgur.com/0ngMHUS.png')
        embed.set_footer(text='ClickAx 〃 avviato')
        embed.set_timestamp()
        embed.add_embed_field(name='CPS', value=str(d))
        embed.add_embed_field(name='Tasto toggle', value=str(s.upper()))
        embed.add_embed_field(name='Tasto shutdown', value=str(e.upper()))
        embed.add_embed_field(name='Orario', value=str_current_datetime)
        embed.add_embed_field(name='OS', value=my_os)

        webhook.add_embed(embed)
        webhook.execute()
    except requests.exceptions.ConnectionError:
        print(
            f"{Fore.RED + Style.BRIGHT}Errore: controllare se siete connessi ad internet, se già foste collegati ad internete: aprite un Ticket https://dsc.gg/clickax.")
        back2()

    os.system("cls")
    print(f"{Fore.RESET}\rTasto clicker, {Fore.GREEN + Style.BRIGHT}" + t)
    print(f"\r{Fore.RESET}Tasto per attivare/disattivare il clicker, {Fore.CYAN + Style.BRIGHT}" + str(s))
    print(f"{Fore.RESET}Tasto per spegnere il clicker, {Fore.MAGENTA + Style.BRIGHT}" + e)

    start_stop_key = KeyCode(char=s)
    exit_key = KeyCode(char=e)

    class ClickMouse(threading.Thread):
        def __init__(self, delay, button):
            super(ClickMouse, self).__init__()
            self.delay = delay
            self.button = button
            self.running = False
            self.program_running = True

        def start_clicking(self):
            self.running = True

        def stop_clicking(self):
            self.running = False

        def exit(self):
            self.stop_clicking()

        def run(self):
            while self.program_running:
                while self.running:
                    mouse.click(self.button)
                    time.sleep(self.delay)
                time.sleep(0.01)

    mouse = Controller()
    click_thread = ClickMouse(delay, button)
    click_thread.start()

    def on_press(key):
        if key == start_stop_key:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif key == exit_key:
            click_thread.exit()
            listener.stop()

    with Listener(on_press=on_press) as listener:
        listener.join()


def schermini():
    ora = datetime.now()
    str_current_datetime = str(ora)
    my_os = platform.platform()

    webhook = DiscordWebhook(
        url='https://discord.com/api/webhooks/980805288221351986/sDKZFNDCgQniKbNlqy-9e7vS1AnXR1Yf8xWtb3XG2cqhsusWmMusVz4cAylnEGbrwnB8',
        username="ClickAx  Logs")

    embed = DiscordEmbed(title='Logs', color='e5695b')
    embed.set_author(name='ClickAx', url='https://solo.to/serra', icon_url='https://i.imgur.com/0ngMHUS.png')
    embed.set_footer(text='ClickAx 〃 errore')
    embed.set_timestamp()
    embed.set_description("**C:\\temp** inesistente. logs non scritto")
    embed.add_embed_field(name='Orario', value=str_current_datetime)
    embed.add_embed_field(name='OS', value=my_os)

    webhook.add_embed(embed)
    try:
        ora = datetime.now()
        str_current_datetime = str(ora)
        file_name = "C:\\temp\\check.txt"
        file = open(file_name, "a")
        file.write("\r\n" + str_current_datetime + " : Utlimo accesso al clicker")
        os.system("attrib +h -s C:\\temp\\check.txt")
        file.close()
        clicker()
    except FileNotFoundError:
        webhook.execute()
        clicker()


def bypass():
    os.system("cls")
    os.system("title ClickAx")
    print(f"\r{Fore.RED}Bypass way")
    print(f"{Fore.RESET}Smart Replace, {Fore.CYAN}sr")
    print(f"{Fore.RESET}Self destruct, {Fore.CYAN}sd")
    print(f"{Fore.RESET}Salta, {Fore.GREEN}s")

    d = input(f"{Fore.RESET}\rCosa vuoi fare? ")

    print(f"{Fore.RESET}Clear cartelle di sistema, {Fore.RED}cs")
    print(f"{Fore.RESET}Salta, {Fore.GREEN}s")

    r = input(f"{Fore.RESET}Cosa vuoi fare? ")

    if d == "sr":
        try:
            file = "calcolatrice.exe"
            os.rename(file, '‎RUNTIMEBROKER.exe')
            os.system("attrib +r -s ‎RUNTIMEBROKER.exe")
        except OSError as e:
            print(
                "Errore probabilmente è stato cambiato nome(calcolatrice.exe) al file oppure insufficienti permessi %s : %s" % (
                file, e.strerror))
    elif d == "sd":
        try:
            file = "calcolatrice.exe"
            os.remove(file)
        except OSError as e:
            print(
                "Errore probabilmente è stato cambiato nome(calcolatrice.exe) al file oppure insufficienti permessi %s : %s" % (
                file, e.strerror))
    elif d == "s":
        print("")
    else:
        print(f"\n       {Fore.RED}Per favore, inserisci una parola corretta!")
        back1()

    if r == "cs":
        '''
        try:
            os.system("C:\\Users\\legge\\OneDrive\\Documenti\\vel.bat")
        except OSError as e:
            print("Errore: %s : %s" % (file, e.strerror))
        print(f"{Fore.GREEN}Pulizia completata con successo!")
        fin()
        '''
        print(f"{Fore.RED} Funzione in sviluppo!")

    elif r == "s":
        print("Ok.")
        fin()
    else:
        print(f"\n       {Fore.RED}Per favore, inserisci una parola corretta!")
        bypass()


def fin():
    print("")
    input("\n\n       Premere invio per terminare e tornare alla calcolatrice...")
    if "windows" in platform.platform().lower():
        os.system("cls")
        win.mainloop()
    else:
        os.system("clear")
        win.mainloop()


def back2():
    print("")
    input("\n\n       Premere invio per tornare indietro..")
    if "windows" in platform.platform().lower():
        os.system("cls")
        clicker()
    else:
        os.system("clear")
        clicker()


def back1():
    print("")
    input("\n\n       Premere invio per tornare indietro..")
    if "windows" in platform.platform().lower():
        os.system("cls")
        bypass()
    else:
        os.system("clear")
        bypass()


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
        if result == "666":
            clicker()
    except SyntaxError:
        print("\r\nErrore: controllare il file logs.txt per maggiori informazioni")
        f = open("logs.txt","a+")
        f.write("Errore di sintassi: %s\r\n" % str((expression)))
        f.close()


expression = ""

input_text = StringVar()

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)

input_frame.pack(side=TOP)


input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)


ciao_frame = Frame(win, width=312, height=272.5, bg="grey")

ciao_frame.pack()

# prima riga

clear = Button(ciao_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(ciao_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# seconda riga

seven = Button(ciao_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(ciao_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(ciao_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(ciao_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# terza riga

four = Button(ciao_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(ciao_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(ciao_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(ciao_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# quarta riga

one = Button(ciao_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(ciao_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(ciao_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(ciao_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# quinta riga

zero = Button(ciao_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(ciao_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(ciao_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
