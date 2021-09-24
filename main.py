import sqlite3
from pynput import keyboard
import pygame

conn=sqlite3.connect("resources/database.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Sounds (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, key TEXT, file TEXT)")
conn.commit()

class MyException(Exception): pass

def on_press(key):
    if key == keyboard.Key.esc:
        raise MyException(key)
    else :
        keyVar = str(key)
        if (keyVar.find("Key.") != -1):
            keySort = keyVar[4:]
        else:
            keySort = keyVar[1]
        try:
            cur.execute("SELECT file FROM Sounds WHERE key= ?", keySort)
            conn.commit()
            sound = cur.fetchall()
            sound = sound[0][0]
            print(sound)
            pygame.mixer.init()
            pygame.mixer.music.load(sound) #mp3 aussi
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
        except:
            print("Pas de touche associée")
        print(keySort)


with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))

cur.close()
conn.close()