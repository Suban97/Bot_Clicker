import threading

from interne.Bot_Clicker import start_bot

    

def run_win():
    from interne.Window import Win 
    Win()


#def run_bot():
 #   start_bot()



target_win= threading.Thread(target=run_win, daemon=True)
target_bot = threading.Thread(target=start_bot, daemon=True)

target_win.start()
target_bot.start()
