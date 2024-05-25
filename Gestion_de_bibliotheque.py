# Classe de base pour tous les éléments de la bibliothèque
class ItemBibliotheque():
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






