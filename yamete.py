# Créé par toinot.gury, le 17/09/2021 en Python 3.7
from pynput import keyboard
import pygame
import sqlite3

class MyException(Exception): pass

def on_press(key):
    if key == keyboard.Key.esc:
        cur.close()
        conn.close()
        raise MyException(key)
    else :
        keyVar = str(key)
        if (keyVar.find("Key.") != -1):
            keySort = keyVar[4:]
        else:
            keySort = keyVar[1]
        try:
            cur.execute("SELECT way FROM Sounds WHERE key = ?", (keySort,))
            conn.commit()
            liste = cur.fetchall()
            sound = liste[0][0]
            pygame.mixer.init()
            pygame.mixer.music.load(sound) #mp3 aussi
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
        except:
            print("Pas de touche associée")
        print(keySort)

# Collect events until released
conn = sqlite3.connect("Yamete_DB.db")         
cur = conn.cursor()                          
with keyboard.Listener(
        on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))
