import random
import string
import time
import pygetwindow as gw
import keyboard
import mouse  # Neue Bibliothek für Mausklicks
from colorama import init, Style
import threading  # Zum Erstellen von Threads für die Bot-Logik

init(autoreset=True)

# ANSI Escape Codes für Farben
PINK = "\033[38;2;255;105;180m"  # RGB für Pink
INFO = "\033[38;2;91;206;250m"  # RGB für Hellblau
ORANGE = "\033[38;2;255;165;0m"  # RGB für Orange

# Generiere einen zufälligen Fenstertitel
def random_window_title():
    length = random.randint(12, 36)
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Setze Fenstertitel
window_title = random_window_title()
print(f"\033]0;{window_title}\007")  # Setzt den Konsolen-Titel auf random title

# ASCII-Logo mit Farbverlauf
ascii_logo = r"""
__________                           __________.____   __________        __          
\______   \___.__.______   __________\______   \    |  \______   \ _____/  |_  ______
 |     ___<   |  |\____ \_/ __ \_  __ \       _/    |   |    |  _//  _ \   __\/  ___/
 |    |    \___  ||  |_> >  ___/|  | \/    |   \    |___|    |   (  <_> )  |  \___ \ 
 |____|    / ____||   __/ \___  >__|  |____|_  /_______ \______  /\____/|__| /____  >
           \/     |__|        \/             \/        \/      \/                 \/ 
           
"""

# Funktion zum Drucken des Logos mit Farbverlauf
def print_gradient_logo(logo_text, start_color, end_color):
    start_rgb = start_color
    end_rgb = end_color
    lines = logo_text.splitlines()
    for i, line in enumerate(lines):
        ratio = i / len(lines)
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)
        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + line + Style.RESET_ALL)

# Farben: Pink bis Hellgelb
print_gradient_logo(ascii_logo, (255, 105, 180), (255, 255, 102))

# Suche nach Rocket League Prozess
print(INFO + "[i] Version: 0.21a" + Style.RESET_ALL)
print(INFO + "[i] Created by Pyperhop <3" + Style.RESET_ALL)
print(INFO + "[i] Join my discord server for support & help! -> https://discord.gg/dgC8Tx4REb" + Style.RESET_ALL)
print(PINK + "[+] Generated Random Name for Console Window to stay undetected." + Style.RESET_ALL)
print(PINK + "[+] Searching Rocket League.exe..." + Style.RESET_ALL)
rocket_window = None
for window in gw.getAllWindows():
    if "Rocket League" in window.title:
        rocket_window = window
        break

# Wenn Fenster gefunden
if rocket_window:
    resolution = f"{rocket_window.width}x{rocket_window.height}"
    print(PINK + f"[+] Found Rocket League! PID {rocket_window._hWnd} on {resolution}" + Style.RESET_ALL)
    print(PINK + "[+] Loaded External Bot Logic into Mouse & Keyboard successfully!" + Style.RESET_ALL)
    print(INFO + "[i] Please keep in mind these Bots are external and use your real Keyboard & Mouse!" + Style.RESET_ALL)
    print(INFO + "[i] Don't tab out of Rocket League to prevent bugs." + Style.RESET_ALL)
    print(INFO + "[i] If you want to switch bots midgame use F2 but disable the other bot first." + Style.RESET_ALL)
    print(INFO + "[i] Do not press any buttons or use your mouse while the bot is enabled! Disable it first." + Style.RESET_ALL)
    print(INFO + "[i] Only use F1 & F2 ingame, always minimize the console window." + Style.RESET_ALL)

    # Funktion zur Bot-Auswahl
    def choose_bot():
        global bot_type
        print(ORANGE + "Please choose a bot to activate! (You can change this later)" + Style.RESET_ALL)
        print(ORANGE + "1 - Meina 620142 + (Heatseeker Kickoff XP Farm)" + Style.RESET_ALL)
        print(ORANGE + "2 - MeinaMix 731273 ++ (Rumble XP Farm)" + Style.RESET_ALL)
        bot_choice = input(ORANGE + "Enter bot number: " + Style.RESET_ALL)

        # Festlegen des Bot-Typs
        if bot_choice == '1':
            bot_type = 'meina'
            print(PINK + "[+] 'Meina 620142 +' Bot selected." + Style.RESET_ALL)
        elif bot_choice == '2':
            bot_type = 'meinamix'
            print(PINK + "[+] 'MeinaMix 731273 ++' Bot selected." + Style.RESET_ALL)
        else:
            print("\033[38;2;255;0;0m[!] Invalid choice. Please restart and select one of the listed bots!" + Style.RESET_ALL)
            exit()

    # Erste Bot-Auswahl aufrufen
    choose_bot()

    # Bot-Status
    bot_running = False

    # Toggle-Funktion
    def toggle_bot():
        global bot_running
        bot_running = not bot_running
        if bot_running:
            print("\033[38;2;0;255;0m[O] Bot enabled!" + Style.RESET_ALL)
            if bot_type == 'meina':
                keyboard.press('w')  # Halte 'W' gedrückt
                threading.Thread(target=spam_left_clicks).start()  # Starte das Linksklick-Spamming
                threading.Thread(target=perform_right_clicks_meina).start()  # Starte die Rechtsklicks
            elif bot_type == 'meinamix':
                keyboard.press('w')  # Halte 'W' gedrückt für MeinaMix
                # Starte die Funktion für Linksklicks in einem neuen Thread
                threading.Thread(target=hold_left_click).start()
                # Starte die Funktion für Rechtsklicks in einem neuen Thread
                threading.Thread(target=perform_right_clicks).start()
                # Starte die Funktion für abwechselnde Tastendrücke in einem neuen Thread
                threading.Thread(target=alternate_key_presses).start()
                # Starte die Funktion für Leertaste in einem neuen Thread
                threading.Thread(target=press_space_randomly).start()
                # Starte die Funktion für R-Taste in einem neuen Thread
                threading.Thread(target=press_r_randomly).start()
        else:
            print("\033[38;2;139;0;0m[X] Bot disabled!" + Style.RESET_ALL)
            keyboard.release('w')  # Lass 'W' los

    # Funktion zur Bot-Umschaltung
    def switch_bot():
        global bot_type
        print(ORANGE + "Please choose a bot to activate! (You can change this later)" + Style.RESET_ALL)
        print(ORANGE + "1 - Meina 620142 + (Heatseeker Kickoff XP Farm)" + Style.RESET_ALL)
        print(ORANGE + "2 - MeinaMix 731273 ++ (Rumble XP Farm)" + Style.RESET_ALL)
        bot_choice = input(ORANGE + "Enter bot number: " + Style.RESET_ALL)

        # Festlegen des Bot-Typs
        if bot_choice == '1':
            bot_type = 'meina'
            print(PINK + "[+] 'Meina 620142 +' Bot selected." + Style.RESET_ALL)
        elif bot_choice == '2':
            bot_type = 'meinamix'
            print(PINK + "[+] 'MeinaMix 731273 ++' Bot selected." + Style.RESET_ALL)
        else:
            print("\033[38;2;255;0;0m[!] Invalid choice. Please select one of the listed bots!" + Style.RESET_ALL)
            return  # Abbrechen, wenn die Auswahl ungültig ist

    # Funktion für Linksklick-Spamming für Meina 620142 +
    def spam_left_clicks():
        while bot_running and bot_type == 'meina':
            mouse.click(button='left')  # Führe einen Linksklick aus
            time.sleep(random.uniform(0.01, 0.20))  # Warte zufällig zwischen 0.01 und 0.20 Sekunden

    # Funktion für Rechtsklicks für Meina 620142 +
    def perform_right_clicks_meina():
        while bot_running and bot_type == 'meina':
            mouse.click(button='right')  # Führe einen Rechtsklick aus
            time.sleep(random.uniform(1, 2))  # Warte zufällig zwischen 1 und 2 Sekunden

    # Funktion für Linksklick-Spamming für MeinaMix
    def hold_left_click():
        while bot_running and bot_type == 'meinamix':
            mouse.click(button='left')  # Führe einen Linksklick aus
            time.sleep(0.01)  # Warte 10 Millisekunden

    # Funktion für Rechtsklicks für MeinaMix
    def perform_right_clicks():
        while bot_running and bot_type == 'meinamix':
            mouse.click(button='right')  # Führe einen Rechtsklick aus
            time.sleep(random.uniform(1, 2))  # Warte zufällig zwischen 1 und 2 Sekunden

    # Funktion für abwechselnde Tastendrücke für MeinaMix
    def alternate_key_presses():
        while bot_running and bot_type == 'meinamix':
            keyboard.press('e')  # Halte die Taste 'E' gedrückt
            time.sleep(0.1)  # Halte 'E' für 100 Millisekunden
            keyboard.release('e')  # Lass die Taste 'E' los
            time.sleep(random.uniform(0.5, 1.5))  # Warte zufällig zwischen 0.5 und 1.5 Sekunden

    # Funktion für Leertaste für MeinaMix
    def press_space_randomly():
        while bot_running and bot_type == 'meinamix':
            keyboard.press('space')  # Drücke die Leertaste
            time.sleep(0.1)  # Halte die Leertaste für 100 Millisekunden
            keyboard.release('space')  # Lass die Leertaste los
            time.sleep(random.uniform(1, 2))  # Warte zufällig zwischen 1 und 2 Sekunden

    # Funktion für R-Taste für MeinaMix
    def press_r_randomly():
        while bot_running and bot_type == 'meinamix':
            keyboard.press('r')  # Drücke die R-Taste
            time.sleep(0.1)  # Halte die R-Taste für 100 Millisekunden
            keyboard.release('r')  # Lass die R-Taste los
            time.sleep(random.uniform(1, 2))  # Warte zufällig zwischen 1 und 2 Sekunden

    # Hauptprogramm-Loop
    try:
        while True:
            if keyboard.is_pressed('f1'):  # F1-Taste für Bot-Umschaltung
                toggle_bot()
                time.sleep(1)  # Kurze Pause, um wiederholte Eingaben zu verhindern
            elif keyboard.is_pressed('f2'):  # F2-Taste für Bot-Wechsel
                switch_bot()
                time.sleep(1)  # Kurze Pause, um wiederholte Eingaben zu verhindern
    except KeyboardInterrupt:
        print("\033[38;2;255;0;0m[!] Bot stopped!" + Style.RESET_ALL)
