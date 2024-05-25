# Classe Livre qui hérite de ItemBibliotheque
class Livre(ItemBibliotheque):
    def __init__(self, titre, auteur, isbn, editeur):
        super().__init__(titre, auteur, isbn)  # Appel du constructeur de la classe parent
        self.editeur = editeur  # Editeur spécifique au Livre
