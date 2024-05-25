#abstraction
from abc import ABC
class listes(ABC):
    def test():
        print("Ceci est un livre")

# Classe de base pour tous les éléments de la bibliothèque
class ItemBibliotheque(listes):
    def __init__(self, titre, auteur, isbn):
        self.titre = titre  
        self.auteur = auteur  
        self.isbn = isbn  
        self.disponible = "disponible" 

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





