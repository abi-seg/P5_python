etudiants = {
    "Alice":{"Maths": 15,"Physique": 14,"Français": 16},
    "Bob":{"Maths": 12, "Physique": 13, "Français": 11},
    "Charlie":{"Maths": 17, "Physique": 16, "Français": 18}
}

nom = input("Entrez le nom de l'étudiant :")

if nom in etudiants:
    print(f"-------Notes de {nom}------- ")
    notes = etudiants[nom]
    total = 0
    for matiere, note in notes.items():
        print(f"{matiere} : {note}")
        total += note
    moyenne = total / len(notes)
    print(f"Moyenne de {nom} : {moyenne}")
else:
    print(f"L'étudiant {nom} n'existe pas dans la liste.")
