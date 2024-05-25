# Exemple d'abstraction et d'encapsulation: les détails de l'implémentation de la classe sont cachés
# et une interface simple est présentée à l'utilisateur de la classe.

# Création d'instances de Livre et DVD
livre1 = Livre("1984", "George", "1289", "Éditions fridy/uniluk")
dvd1 = DVD("Inception", "Christopher Nolan", "987654321", 148)

# Exemple d'emprunt et de retour
livre1.emprunter()
dvd1.emprunter(25)
print(verifier_disponibilite(livre1))  # Affiche False car le livre a été emprunté
print(verifier_disponibilite(dvd1))
