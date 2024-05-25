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