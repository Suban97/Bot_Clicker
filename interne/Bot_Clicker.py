import pyautogui
import keyboard
import threading
import time

import os, webbrowser, sys

print(os,  webbrowser, sys)
# 📸 Chemin vers l'image du cookie
Cookie = os.path.join("interne", "ressources", "Cookie.png")

# 🧪 Debug - peut être désactivé après test
print(f"[DEBUG] Cookie path: {Cookie}")

def start_bot():
    print("Fonction du bot lancé")
    print(f"[INFO] Utilisation de l'image : {Cookie}")

    # 🌐 Lance Cookie Clicker
    url = "https://orteil.dashnet.org/cookieclicker/"
    webbrowser.open(url)
    print("[INFO] Lancement de Cookie Clicker...")

    pause = False

    # ⏸ Fonction pause déclenchée par Maj+w
    def pause_fonction():
        nonlocal pause
        while True:
            keyboard.wait('Maj+w')
            print("[INFO] Pause...")
            pause = True
            time.sleep(1)
            SLEEP()
            pause = False
            print("[INFO] Reprise.")

    threading.Thread(target=pause_fonction, daemon=True).start()

    # 🔎 Localisation de l'image
    located_Cookie = None
    while not located_Cookie:
         try:
            
            located_Cookie = pyautogui.locateOnScreen(Cookie, confidence=0.4)
            
            if located_Cookie:
                print("[INFO] Cookie trouvé !")

         except Exception as e:
             print(f"[ERREUR Cookie non trouvé] {e}")
             time.sleep(0.5)



    # 🖱 Boucle de clic
    while True:
        if keyboard.is_pressed("Maj+q"):
            print("[INFO] Arrêt du bot.")
            sys.exit()
        if not pause:
            pyautogui.click(pyautogui.center(located_Cookie))
        time.sleep(0.03)



def SLEEP():
    keyboard.wait("Maj+w")
    

# Ne pas lancer automatiquement
# Lance start_bot() # manuellement
if __name__ == "__main__":
    start_bot()
