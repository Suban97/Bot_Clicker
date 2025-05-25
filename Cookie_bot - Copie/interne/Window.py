from tkinter import *
import keyboard
import threading




print("window demarre...")

########################################################################################################################

    
    
def Win():   

    # Créer la fenêtre
    window = Tk()
    window.title("Command")
    window.geometry("440x340")



    # Ajouter le texte
    Label_title = Label(window, wraplength=350, text="Commandes disponibles", font=("Arial", 30, "bold"))
    Label_commandes = Label(window, wraplength=350, text="\nAfficher et masquer cette page: Maj+M \nMarquer une pause de 30 secondes  : Maj+Q \nStopper le programme : Maj+W", anchor="w", justify="left", width=30, font=('Arial', 20))


    Label_title.pack(expand=True, fill='both')
    Label_commandes.pack(expand=True, fill='both')



    # Masquer la fenêtre au démarrage
    window.withdraw()

    def detection():
        while True:
            keyboard.wait("Maj+x")# Attend que "Maj + x" soit pressé
            window.after(0, toggle_window)  # Demande au thread principal de modifier l'UI

    def toggle_window():
        if window.state() == "withdrawn":  
            window.deiconify()  # Affiche la fenêtre
            window.attributes("-topmost", True)
            print("fenêtre affiché")
        else:
            window.withdraw()
            print("fenêtre masquée")# Cache la fenêtre



    # Lancer le thread de détection clavier
    threading.Thread(target=detection, daemon=True).start()



    # Exécuter Tkinter dans le thread principal
    window.mainloop()

Win()
