# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import cst
import numpy as np


class Tuile:
    def __init__(self, nombre : int, color : int):
        if not isinstance(color, int ):
            raise ValueError("Le paramètre 'color' doit être un nombre.")
        if not isinstance(nombre, int):
            raise ValueError("Le paramètre 'nombre' doit être un nombre")
        if nombre not in cst.nombres or color not in cst.true_colors.keys() or nombre == 0 and color in [1, 2]:
            raise ValueError("La tuile n'est pas dans le jeu")
        self.nombre = nombre
        self.color = color
    

    
    
    def isJoker(self):
        if self.nombre == 0 and self.color in [3, 4]:
            return True
        else: 
            return False
    
    def __str__(self):
        if self.isJoker():
            return f"Joker {cst.true_colors[self.color]}"
        else:
            return f"{self.nombre} {cst.true_colors[self.color]}"
    def __eq__(self, o):
        return self.nombre == o.nombre and self.color == o.color

class Set:
    def __init__(self, tuiles : list):
        self.tuiles = tuiles
        
    def ajout_tuile(self, tuile:Tuile):
        self.tuiles.append(tuile)
    
    def retr_tuile(self, tuile:Tuile):
        if not tuile in self.tuiles :
            raise ValueError("la tuile n'est pas dans le set")       
        else:
            self.tuiles.remove(tuile)
    def validate (self):
        colors = []
        nbs = []
        tuiles_array = np.array(self.tuiles)
        for i in range (len(self.tuiles)):
            dup_tuiles = self.tuiles
            dup_tuiles.pop(i)
            for j in range (len(self.tuiles)):
                if self.tuiles[i] == dup_tuiles[j]:
                    return False
                else:
                    next
                
        for t in self.tuiles:
            nbs.append(t.nombre)
            colors.append(t.color)
            
        Min = nbs[0]
        Max = max(nbs)
        taille = len(self.tuiles)
        print(nbs, colors, Min, Max, taille)
        
        if Min == 0 or Max ==0 :
            return False
        if Min < Max :
            verif_suite = np.array(cst.nombres[Min:Max+1]) - np.array(nbs)
            check_suite = np.where(verif_suite != 0)
            if taille < 3 :      
                return False
                
            if len(check_suite) > 2 :
                return False
            if not check_suite :
                return True
            else :
                
                joker_check  = tuiles_array[check_suite]
                for el in joker_check:
                   val =  el.isJoker()
                return val
               
        if Min == Max :
            compte_colors = np.unique(colors,return_counts = True)
            
            print(compte_colors)
            if 2 > taille > 4 :
                return False
            
            verif_meme =  np.ones(taille) * Min - nbs 
            check_meme = np.where(verif_meme != 0)
            
            if len(check_meme) > 2 :
                return False
            if not check_meme :
                return True
            else :
                joker_check  = tuiles_array[check_meme]
                for el in joker_check:
                   val =  el.isJoker()
                return val
                
            

            
        
    def __str__(self):
        if not self.tuiles:
            return "Le set est vide"
        else :
            return "\n".join(str(e) for e in self.tuiles)

class Pioche:
    def __init__(self):
        self.pioche = []
        for c in cst.true_colors.keys():
            for n in cst.nombres:
                if not (n == 0 and c in [1,2]):
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
    
    def check_table(self, table):
        for s in self.table:
            for t in self.table.Set:
                check1 += len(t)
        for s in table:
            for t in table.Set:
                check2 += len(t)
        return check1-check2
    

        
    
tuile3 = Tuile(0, 3)

tuile4 = Tuile(0, 4)


# Création et ajout de tuiles
tuile1 = Tuile(12, 3)


tuile2 = Tuile(12, 3)

tuile5 = Tuile(8, 3)


pioche = Pioche()

set1 = Set([tuile2,tuile3,tuile1])

print(set1)
print(set1.validate())