import threading

from interne.Bot_Clicker import start_bot

    
print("Programme lance")

def run_win():
    from interne.Window import Win 
    Win()


def run_bot():
    from interne.Bot_Clicker import start_bot
    start_bot()



target_bot = threading.Thread(target=run_bot)





target_bot.start()
run_win()
target_bot.join()
print("Threads started.")
