# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import cst
import numpy as np


class Tuile:
    def __init__(self, nombre : int, color : str):
        if not isinstance(color, str):
            raise ValueError("Le paramètre 'color' doit être une chaîne de caractères.")
        if not isinstance(nombre, int):
            raise ValueError("Le paramètre 'nombre' doit être un nombre")
        if nombre not in cst.nombres or color not in cst.colors or nombre == 0 and color in ["bleu", "orange"]:
            raise ValueError("La tuile n'est pas dans le jeu")
        self.nombre = nombre
        self.color = color
    

    
    
    def isJoker(self):
        return self.nombre == 0 and self.color in ["noir", "rouge"]
    
    def __str__(self):
        if self.isJoker():
            return f"Joker {self.color}"
        else:
            return f"{self.nombre} {self.color}"
        

class Set:
    def __init__(self):
        self.tuiles = []
    
    def ajout_tuile(self, tuile:Tuile):
        self.tuiles.append(tuile)
    
    def retr_tuile(self, tuile:Tuile):
        if not tuile in self.tuiles :
            raise ValueError("la tuile n'est pas dans le set")       
        else:
            self.tuiles.remove(tuile)
    def 
    def __str__(self):
        if not self.tuiles:
            return "Le set est vide"
        else :
            return "\n".join(str(e) for e in self.tuiles)

class Pioche:
    def __init__(self):
        self.pioche = []
        for c in cst.colors:
            for n in cst.nombres:
                if not (n == 0 and c in ["bleu", "orange"]):
                    self.pioche.append(Tuile(n,c))
    def tirer(self):
        if not self.pioche:
            raise ValueError("La pioche est vide.")
        
        tuile_tiree = np.random.choice(self.pioche)
        self.pioche.remove(tuile_tiree)
        return tuile_tiree
        
    def __str__(self) :
        if not self.pioche:
            return "La pîoche est vide"
        else :
            return "\n".join(str(e) for e in self.pioche)

class Table:
    def __init__(self):
        self.table = []
    
    def ajout_set (self, tuiles: Set):
        self.table.appends(tuiles)
    
    def check_table(self, table : Table):
        for s in self.table:
            for t in self.table.Set:
                check1 += len(t)
        for s in table:
            for t in table.Set:
                check2 += len(t)
        return check1-check2
    
    def validate
        
    
tuile3 = Tuile(0, 'rouge' )

set_de_tuiles = Set()

# Création et ajout de tuiles
tuile1 = Tuile(12, "rouge")
set_de_tuiles.ajout_tuile(tuile1)

tuile2 = Tuile(13, "noir")
set_de_tuiles.ajout_tuile(tuile2)

set_de_tuiles.ajout_tuile(tuile3)

pioche = Pioche()


print(pioche.tirer())
print(pioche)