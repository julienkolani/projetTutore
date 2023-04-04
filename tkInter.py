import tkinter as tk

# Définition des variables globales
mail_entry = None
name_entry = None
telephone_entry = None

def get_data():
    # récupère les données des champs d'entrée en utilisant les variables globales
    global mail_entry, name_entry, telephone_entry
    mail = mail_entry.get()
    ip = name_entry.get()
    telephone = telephone_entry.get()

    # affiche les données récupérées dans la console
    print("Mail:", mail)
    print("IP:", ip)
    print("Téléphone:", telephone)

    # efface les champs d'entrée
    mail_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    telephone_entry.delete(0, tk.END)

def create_window():
    global mail_entry, name_entry, telephone_entry
    # crée la fenêtre Tkinter
    root = tk.Tk()
    root.title("Données utilisateurs")
    root.geometry("360x150")
    root.minsize(210, 100)
    root.configure(bg="#202123")

    # ajoute un label pour indiquer ce qu'il faut entrer
    mail_label = tk.Label(root, text="Entrez votre Mail :", bg="#202123", fg="white", font=("Arial", 12, "bold"))
    mail_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # ajoute un champ d'entrée pour saisir le mail
    mail_entry = tk.Entry(root, font=("Arial", 12))
    mail_entry.grid(row=0, column=1, padx=10, pady=10)

    # ajoute un label pour indiquer ce qu'il faut entrer
    name_label = tk.Label(root, text="Entrez votre IP :", bg="#202123", fg="white", font=("Arial", 12, "bold"))
    name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    # ajoute un champ d'entrée pour saisir l'ip
    name_entry = tk.Entry(root, font=("Arial", 12))
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    """ # ajoute un label pour indiquer ce qu'il faut entrer
        telephone_label = tk.Label(root, text="Entrez votre téléphone :", bg="#202123", fg="white", font=("Arial", 12, "bold"))
        telephone_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # ajoute un champ d'entrée pour saisir le téléphone
        telephone_entry = tk.Entry(root, font=("Arial", 12))
        telephone_entry.grid(row=2, column=1, padx=10, pady=10)"""

    # ajoute un bouton pour envoyer les données
    submit_button = tk.Button(root, text="Envoyer", command=get_data, bg="green", fg="white", font=("Arial", 12, "bold"))
    submit_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

    # lance la boucle principale Tkinter
    root.mainloop()

# Appelle la fonction

create_window()


