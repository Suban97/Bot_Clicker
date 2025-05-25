import pyautogui, keyboard, threading, subprocess, time



# 📸 Chemin vers l'image du cookie
Cookie = "interne/ressources/Cookie.png"

# 🧪 Debug - peut être désactivé après test
print(f"[DEBUG] Cookie path: {Cookie}")

def start_bot():
    print(f"[INFO] Utilisation de l'image : {Cookie}")

    # 🌐 Lance Cookie Clicker
    url = "https://orteil.dashnet.org/cookieclicker/"
    subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe", url])

    pause = False

    # ⏸ Fonction pause déclenchée par Maj+w
    def pause_fonction():
        nonlocal pause
        while True:
            keyboard.wait('Maj+w')
            print("[INFO] Pause...")
            pause = True
            time.sleep(20)
            pause = False
            print("[INFO] Reprise.")

    threading.Thread(target=pause_fonction, daemon=True).start()

    # 🔎 Localisation de l'image
    located_Cookie = None
    while not located_Cookie:
         try:
            located_Cookie = pyautogui.locateOnScreen(Cookie, confidence=0.5)
            if located_Cookie:
                print("[INFO] Cookie trouvé !")
         except Exception as e:
             print(f"[ERREUR] {e}")



    # 🖱 Boucle de clic
    while True:
        if keyboard.is_pressed("Maj+q"):
            print("[INFO] Arrêt du bot.")
            break
        if not pause:
            pyautogui.click(pyautogui.center(located_Cookie))
        time.sleep(0.03)




# Ne pas lancer automatiquement
# Lance start_bot() manuellement
