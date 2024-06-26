#abstraction
from abc import ABC
class listes(ABC):
    def test():
        print("Ceci est un livre")

# Classe de base pour tous les éléments de la bibliothèque
class ItemBibliotheque(listes):
    def __init__(self, titre, auteur, isbn):
        """Pratique sur l'encapsulation"""
        self.__titre = titre  
        self.__auteur = auteur  
        self.__isbn = isbn  
        self.__disponible = "disponible" 

    def emprunter(self):
        if self.disponible:
            self.disponible = "n'est pas disponible"  # L'item est maintenant emprunté
            return "disponible"
        return "n'est pas disponible"  # L'item n'est pas disponible

    def retourner(self):
        self.disponible = "disponible"  # L'item est retourné et disponible
# Classe Livre qui hérite de ItemBibliotheque
class Livre(ItemBibliotheque):
    def __init__(self, titre, auteur, isbn, editeur):
        super().__init__(titre, auteur, isbn)  # Appel du constructeur de la classe parent
        self.editeur = editeur  # Editeur spécifique au Livre
# Classe DVD qui hérite de ItemBibliotheque et surcharge la méthode emprunter
class DVD(ItemBibliotheque):
    def __init__(self, titre, auteur, isbn, duree):
        super().__init__(titre, auteur, isbn)  # Appel du constructeur de la classe parent
        self.duree = duree  # Durée spécifique au DVD

    # Surcharge de la méthode emprunter pour inclure une vérification d'âge
    def emprunter(self, age):
        if age < 18:
            return "n'est pas disponible"  # Les utilisateurs de moins de 18 ans ne peuvent pas emprunter de DVD
        return super().emprunter()  # Appel de la méthode emprunter du parent
    # Utilisation du polymorphisme avec une fonction qui traite les items de manière générique
    def verifier_disponibilite(item):
        return item.disponible  # Retourne la disponibilité de l'item, qu'il soit un Livre ou un DVD

# Création d'instances de Livre et DVD
livre1 = Livre("1984", "George", "1289", "Éditions fridy/uniluk")
dvd1 = DVD("Inception", "Christopher Nolan", "987654321", 148)

# Exemple d'emprunt et de retour
livre1.emprunter()
dvd1.emprunter(25)
print(verifier_disponibilite(livre1))  # Affiche False car le livre a été emprunté
print(verifier_disponibilite(dvd1))




