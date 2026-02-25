import tkinter as tk
import keyboard
import threading




print("root demarre...")

########################################################################################################################

    
    
def Win():   

    # Créer la fenêtre
    root = tk.Tk()
    root.title("Command")
    root.geometry("800x800+900+100")
    
    root.configure(bg="black")


    lf = tk.LabelFrame(root, text="Commandes de Bot Clicker", bg = "lightblue", relief="raised",padx=50, pady=50)
    lf.pack(padx=50, pady=50)

    # Ajouter le texte
    Label_title = tk.Label(lf, wraplength=350, text="Commandes disponibles", font=("Arial", 30, "bold"))
    Label_commandes = tk.Label(lf, wraplength=350, text="\nAfficher et masquer cette page: Maj+X \n Activer et désactiver la pause : +Q \nStopper le programme : Maj+W", anchor="w", justify="left", width=30, font=('Arial', 20))


    Label_title.pack(expand=True, fill='both')
    Label_commandes.pack(padx = 100, pady=100 ,expand=True, fill='both')



    # Masquer la fenêtre au démarrage
    root.withdraw()

    def detection():
        while True:
            keyboard.wait("Maj+x")# Attend que "Maj + x" soit pressé
            root.after(0, toggle_root)  # Demande au thread principal de modifier l'UI

    def toggle_root():
        if root.state() == "withdrawn":  
            root.deiconify()  # Affiche la fenêtre
            root.attributes("-topmost", True)
            print("fenêtre affiché")
        else:
            root.withdraw()
            print("fenêtre masquée")# Cache la fenêtre



    # Lancer le thread de détection clavier
    threading.Thread(target=detection, daemon=True).start()



    # Exécuter Tkinter dans le thread principal
    root.mainloop()

Win()

