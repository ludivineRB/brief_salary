# coding: utf-8
 
from tkinter import * 
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import tkinter.font as font
import json
import os
from functions import CalcSalary, csv_creation, stat_subsidiary, stats_globales

fenetre = Tk()

label = Label(fenetre, text="Choississez vos données à analyser:")
label.pack()

def traitement():    # On demande à l'utilisateur de sélectionner un fichier avec la commande askopenfilename, en lui laissant le choix entre Excel et CSV.
    chemin_fichier = askopenfilename(filetypes=[('.json', ('*.json', '*.JSON')), ('CSV', '*.csv')])
     # On lit le fichier dans la variable data
    with open('employes_data_10_2024.json')as file:
        data = json.load(file)


### la on met notre code de traitement ######

def generate_csv(data):
    csv_creation(data)


    # On récupère le chemin d'accès du dossier pour pouvoir générer un fichier Excel dans ce même dossier. 
    chemin_dossier = os.path.dirname(chemin_fichier)


bouton=Button(fenetre, text="salaires", command=traitement)
bouton.pack()




# label
label = Label(fenetre, text="Choissisez la filiale", bg="lightgrey")
label.pack()

'''# canvas
canvas = Canvas(fenetre, width=150, height=120, background='floral white')

txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="dark salmon")

canvas.pack()'''

# créer la liste Python contenant les éléments de la liste Combobox
listeProduits=["TechCorp", "DesignWork","ProjectLead"]
 
# 3) - Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(fenetre, values=listeProduits)
 
# 4) - Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)
 
listeCombo.pack()
"""
btn_generate_csv = tk.Button(root, text="Générer CSV", command=create_csv)
btn_generate_csv.pack(pady=20)
bouton=Button(fenetre, text="salaires", command=fenetre.generate_csv)
bouton.pack()
"""
bouton=Button(fenetre, text="csv", command=fenetre.quit)
bouton.pack()

"""##Fonction pop-up
def popupmsg(msg):
    popup = tk.Tk()    # On définit le titre de la fenêtre
    popup.wm_title("Votre attention s'il vous plait !")  
    # On choisit une couleur de fond à notre fenêtre.    
    popup.configure(background="LemonChiffon2")    # Puis on définit le message que l'on verra apparaître     label_popup = tk.Label(popup, text=msg, foreground = "#641E16", background = "#FA7F7F")    # On définira plus tard une mise en forme standard f_label    label_popup['font'] = f_label    # On ajoute notre texte à la fenêtre avec .pack()    label_popup.pack()    # On ajoute un bouton qui fermera notre fenêtre    bouton_popup = tk.Button(popup, text="C'est compris!", command = popup.destroy)    # On embellit notre bouton    bouton_popup.configure(foreground="#641E16", background = "white")
    bouton_popup['font'] = f_bouton
    bouton_popup.pack()
    popup.mainloop()"""


#fermer
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()


fenetre.mainloop()