import threading

<<<<<<< HEAD
from interne.Bot_Clicker import start_bot

    
=======
print("Programme lance")
>>>>>>> 64cbfa5 (Fix threading issues and improve bot stability)

def run_win():
    from interne.Window import Win 
    Win()


<<<<<<< HEAD
#def run_bot():
 #   start_bot()



target_win= threading.Thread(target=run_win, daemon=True)
target_bot = threading.Thread(target=start_bot, daemon=True)

target_win.start()
target_bot.start()
=======
def run_bot():
    from interne.Bot_Clicker import start_bot
    start_bot()



target_bot = threading.Thread(target=run_bot)





target_bot.start()
run_win()
target_bot.join()
print("Threads started.")
>>>>>>> 64cbfa5 (Fix threading issues and improve bot stability)
