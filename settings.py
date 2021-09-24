from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
import sqlite3

global action
action = 0

def change_label(event):
    global action
    if action == 0:
        global touche
        touche = event.char
        select_key_txt.configure(text=touche, fg="black", font = ("Arial", 25))
        action = 1

def change_touche():
    select_key_txt.configure(text="<Apppuyez sur une touche>", fg="#DCDCDC", font=("Arial",20))
    global action
    action = 0

def definir_touche():
    global action
    if action == 1 :
        filename = askopenfilename()
        data = (touche, filename)
        cur.execute("INSERT INTO Sounds (key, file) VALUES (?, ?)", data)
        conn.commit()
        change_touche()

def reset_touche():
    global action
    global touche
    if action == 1:
        cur.execute("DELETE FROM Sounds WHERE Sounds.key = ?", touche)
        conn.commit()
        showinfo("Rénitialisation touche", "Touche rénitialisée avec succès !")
        change_touche()

conn = sqlite3.connect("resources/database.db", check_same_thread = False)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Sounds (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, key TEXT, file TEXT)")
conn.commit()

fenetre = Tk()
fenetre.title("LOLI Keyboard Settings")
fenetre.geometry("1000x700")
fenetre.resizable(False, False)
fenetre.iconbitmap('resources/ico/loli.ico')
fenetre.config(background="grey")

titre = Label(fenetre, text="LOLI Keyboard Settings", font="Arial 40", bg="grey")
titre.place(relx=0.5, rely=0.1, anchor="center")

change_butt = Button(text="Changer", bd=2, padx=5, pady=5, height=2, width=20, font=("Arial", 15), command=change_touche)
change_butt.place(relx=0.16, rely=0.9, anchor="center")
reset_butt = Button(text="Rénitialiser", bd=2, padx=5, pady=5, height=2, width=20, font=("Arial", 15), command=reset_touche)
reset_butt.place(relx=0.5, rely=0.9, anchor="center")
config_butt = Button(text="Configurer", bd=2, padx=5, pady=5, height=2, width=20, font=("Arial", 15), command=definir_touche)
config_butt.place(relx=0.83, rely=0.9, anchor="center")

select_key_txt = Label(fenetre, text="<Appuyez sur une touche>", font=("Arial", 20), fg="#DCDCDC", bg="grey")
select_key_txt.place(relx=0.5, rely=0.5, anchor="center")

fenetre.bind('<Key>', change_label)

fenetre.mainloop()
cur.close()
conn.close()
