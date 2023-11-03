# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Durée:
    def __init__(self, heures=0, minutes=0, secondes=0):
        self.heures = abs(heures)
        self.minutes = abs(minutes) % 60
        self.secondes = abs(secondes) % 60

    def afficher(self):
        print(f"{self.heures}h{self.minutes:02}m{self.secondes:02}s")

    def en_secondes(self):
        return self.heures * 3600 + self.minutes * 60 + self.secondes

    def ajouter_secondes(self, secondes):
        total_secondes = self.en_secondes() + secondes
        if total_secondes < 0:
            total_secondes = 0
        self.heures = total_secondes // 3600
        self.minutes = (total_secondes % 3600) // 60
        self.secondes = total_secondes % 60

# Exemples d'utilisation
duree1 = Durée(3, 70, -10)
duree1.afficher()  # Affiche : 3h10m10s
print(duree1.en_secondes())  # Affiche : 11410

duree2 = Durée()
duree2.afficher()  # Affiche : 0h00m00s
duree2.ajouter_secondes(3700)
duree2.afficher()  # Affiche : 1h01m40s

