# -*- coding: utf-8 -*-

import cst
import numpy as np
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QColor, QPalette

def from_input():
    """
    Fonction permettant de créer un ensemble de tuiles à partir d'une entrée utilisateur.
    Les tuiles sont entrées sous la forme 'nombre couleur' (exemple: '5 bleu').
    """
    tuiles = []  # Liste des tuiles créées
    print("Entrez les tuiles sous la forme `nombre couleur` (par exemple, `5 bleu`). Tapez 'fin' pour terminer.")
    
    while True:
        data = input("Tuile (ou 'fin' pour terminer) : ")
        if data.lower() == 'fin':  # Sortie de la boucle si l'utilisateur tape 'fin'
            break
        try:
            # Récupération et validation des données de l'utilisateur
            nombre_str, couleur_str = data.split()
            nombre = int(nombre_str)
            color = cst.colors_to_codes.get(couleur_str.lower())  # Conversion de la couleur en code numérique
            
            if color is None:
                raise ValueError(f"Couleur '{couleur_str}' non reconnue.")
                
            # Ajout de la tuile à la liste
            tuiles.append(Tuile(nombre, color))
        except ValueError as e:
            print(f"Entrée invalide : {e}")  # Message d'erreur pour une entrée non valide
    return Set(tuiles)  # Retourne un objet Set contenant les tuiles

def commencer_partie(liste_joueur):
    """
    Fonction pour démarrer une partie.
    Initialise une table, une pioche et une partie, puis distribue les tuiles
    et exécute les tours jusqu'à ce qu'un joueur gagne.
    """
    table = Table([])  # Création d'une table vide
    pioche = Pioche()  # Création d'une pioche
    partie = Partie(liste_joueur, table, pioche)  # Initialisation de la partie avec les joueurs, la table et la pioche
    partie.distribuer()  # Distribution des tuiles aux joueurs
    
    while not partie.isWinner():
        partie.tour_de_jeu(pioche, table)  # Exécute les tours de jeu jusqu'à un gagnant

class Tuile:
    def __init__(self, nombre: int, color: int):
        """
        Initialise une tuile avec un nombre et une couleur.
        Vérifie que les deux sont des entiers.
        """
        if not isinstance(color, int):
            raise ValueError("Le paramètre 'color' doit être un nombre.")
        if not isinstance(nombre, int):
            raise ValueError("Le paramètre 'nombre' doit être un nombre.")
            
        # Initialisation des attributs
        self.nombre = nombre
        self.color = color

    def isTuile(self):
        """
        Vérifie si la tuile est valide selon les règles du jeu.
        """
        # La tuile est valide si elle est dans les numéros de jeu autorisés et couleurs valides
        if (self.nombre not in cst.nombres or 
            self.color not in cst.true_colors.keys() or 
            (self.nombre == 0 and self.color in [1, 2])):  # Vérifie si elle n'est pas un joker
            return False
        else:
            return True

    def isJoker(self):
        """
        Vérifie si la tuile est un joker.
        """
        return self.nombre == 0 and self.color in [3, 4]

    def to_widget(self):
        """
        Transforme la tuile en un widget QLabel pour l'afficher dans l'interface graphique.
        """
        label = QLabel()  # Création d'un QLabel pour représenter la tuile
        
        # Définition de l'affichage pour un joker
        if self.isJoker():
            label.setText(f"Joker {cst.true_colors[self.color]}")
            label.setStyleSheet("background-color: gray; color: white; padding: 10px;")
        else:
            # Affichage pour une tuile classique
            label.setText(f"{self.nombre} {cst.true_colors[self.color]}")
            color = QColor(cst.true_colors[self.color])  # Convertir le nom de couleur en couleur QColor
            palette = QPalette()
            palette.setColor(QPalette.Background, color)  # Définir la couleur de fond du QLabel
            label.setPalette(palette)

    def __str__(self):
        """
        Définit la représentation textuelle de la tuile.
        """
        if self.isJoker():
            return f"Joker {cst.true_colors[self.color]}"
        else:
            return f"{self.nombre} {cst.true_colors[self.color]}"

    def __eq__(self, o):
        """
        Définie l'égalité entre deux tuiles.
        """
        return self.nombre == o.nombre and self.color == o.color
    
    def __hash__(self):
        """
        Définit le hachage pour pouvoir utiliser l'objet Tuile dans des ensembles ou comme clé de dictionnaire.
        """
        return hash((self.nombre, self.color))


class Set:
    #creation d'un set une suite de tuile
    def __init__(self, tuiles : list):
        self.tuiles = tuiles
        
    def ajout_tuile(self, tuile:Tuile):
        self.tuiles.append(tuile)
    
    def retr_tuile(self, tuile:Tuile):
        if not tuile in self.tuiles :
            raise ValueError("la tuile n'est pas dans le set")       
        else:
            self.tuiles.remove(tuile)
     #valide le set si c'est une suite ou le meme chiffre de couleur différentes
#pour la serie il compare la diference entre la suite dans constante et la suite proposé par le joueur dans le set
#pour le meme chiffre il verifie le meme nombre et la meme couleur       
    def validate (self):
        colors = []
        nbs = []
        tuiles_array = np.array(self.tuiles)
        for i in range (len(self.tuiles)):
            dup_tuiles = self.tuiles.copy()
            del dup_tuiles[i]
            for j in range (len(dup_tuiles)):
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
        
        if Min == 0 or Max ==0 :
            return False
        if Min < Max :
            verif_suite = np.array(cst.nombres[Min:Max+1]) - np.array(nbs)
            check_suite = np.where(verif_suite != 0)
            if taille < 3 :      
                return False
                
            if len(check_suite[0]) > 2 :
                return False
            if not len(check_suite[0]) :
                return True
            else :
                
                joker_check  = tuiles_array[check_suite]
                for el in joker_check:
                   val =  el.isJoker()
                return val
               
        if Min == Max :

            
            if 2 > taille > 4 :
                return False
            
            verif_meme =  np.ones(taille) * Min - nbs 
            check_meme = np.where(verif_meme != 0)
            
            if len(check_meme[0]) > 2 :
                return False
            if not len(check_meme[0]) :
                return True
            else :
                joker_check  = tuiles_array[check_meme]
                for el in joker_check:
                   val =  el.isJoker()
                return val
        

    def point(self):
        #compte les points
        nbs = []
        for t in self.tuiles:
            nbs.append(t.nombre)
        return np.sum(nbs)
    
    
    def __str__(self):
        if not self.tuiles :
            return "Le set est vide"
        else :
            return " ".join(str(e) for e in self.tuiles)
        
    def to_widget(self):
        wig = []
        for e in self.tuiles:
            wig.append(e.to_widget())
        return wig
    
class Pioche:
    #distribue toute les combinaisons de tuiles possibles 2 fois pour les tuiles nprmales
    #et definit les 2 jokers
    
    def __init__(self):
        self.pioche = []
        for c in cst.true_colors.keys():
            for n in cst.nombres:
                if Tuile(n,c).isTuile() :
                    if Tuile(n,c).isJoker() :
                        self.pioche.append(Tuile(n,c))
                    else:
                        self.pioche.append(Tuile(n,c))
                        self.pioche.append(Tuile(n,c))
        self.pioche = np.array(self.pioche)
        
    def supp_tuile(self, liste_id : list):
        self.pioche = np.delete(self.pioche,liste_id)
        
    def tirer(self):
        if self.pioche.shape[0] == 0:
            raise ValueError("La pioche est vide.")
        
        tuile_tiree = np.random.choice(self.pioche)
        remv_value = np.where(self.pioche == tuile_tiree)
        try:
            if len(remv_value[0]) == 1 :
                self.pioche = np.delete(self.pioche,remv_value)
            else:
                self.pioche = np.delete(self.pioche,remv_value[0])
            return tuile_tiree
        
        except ValueError as e:
            return e
        
    def __str__(self) :
        if not self.pioche:
            return "La pîoche est vide"
        else :
            return "\n".join(str(e) for e in self.pioche)

class Table:
    #definit la table qui contient les sets et se valides de la même façon que les sets
    #en parcourant les sets sur la table
    def __init__(self, list_set : list):
        self.table = list_set
    
    def ajout_set (self, tuiles: Set):
        self.table.append(tuiles)
    
    def check_table(self):
        if len(self.table) == 0 :
            return True
        else :
            res = []
            for s in self.table:
                res.append(s.validate())
            
            if np.unique(res).shape[0] == 1 :
                return True
            
            else:
                return False
            
    def compare_Table(self, autre_table):
        #pour qu'aucune tuile ne soit recuperer dans la main du joueur. Toutes les tuiles 
        #prrésentes sur la table avant de joué doivent y être après le tour du joueur
        tuiles_presentes = set()
        for set_de_tuiles in self.table:
            tuiles_presentes.update(set_de_tuiles.tuiles)
        
        for autre_set in autre_table.table:
            for tuile in autre_set.tuiles:
                if tuile not in tuiles_presentes:
                    return False
        return True
        
    def __str__(self):
        if not self.table:
            return "La table est vide"
        else :
            return "/n ".join(str(e) for e in self.table)
        
            
        
    

class Joueur:
    def __init__(self, nom : str):
        self.nom = nom
        self.actif = False
        self.debut = False
        self.score = 0
        self.main : Set

        
        
    
    def pose(self, sett : Set, table : Table):
        #le joueur pose un set composé de tuile da²ns sa main
        if sett.validate():
            for s in sett.tuiles:
                self.main.retr_tuile(s)
            table.ajout_set(sett)
            table.check_table()
            self.score += sett.point()
        else: 
            raise ValueError("Le set ne peut être joué car il est invalide.Tenez de joouez une autre combinaison ou piocher")
    
    def pioche(self, tuile : Tuile):
        self.main.ajout_tuile(tuile)
        
    
    def __str__(self):
        return  f"{self.nom} a un score de {self.score}"
    
class Partie:
    def __init__(self, liste_joueur : list, table : Table, pioche : Pioche):
        self.liste_joueur = liste_joueur
        self.table = table
        self.pioche = pioche
        self.j_actif = ""
        self.tour = 0
    
    def add_joueur(self, joueur : Joueur):
        self.liste_joueur.append(joueur)
        
    def distribuer(self):
        i = 0
        for j in self.liste_joueur :
            ind_aleatoires = np.random.choice(range(106 - i * 14), 14, replace=False)
            j.main = Set(self.pioche.pioche[ind_aleatoires].tolist())
            self.pioche.supp_tuile(ind_aleatoires)
            i +=1
            
    def isWinner(self):
        #verifie qu'un joueur gagne
        for j in self.liste_joueur:
            if len(j.main.tuiles) == 0 and self.table.check_table() :
                return True
            else:
                next
            
    def tour_de_jeu(self):
        #definit les actions de jeu poser, piocher, retirer ou ajouté une tuile à la table
        
        for joueur in self.liste_joueur:
            joueur.actif = True  # Activer le joueur au début de son tour
            print(f"\nTour de {joueur.nom} - Score: {joueur.score}")
            
            
            current_set = Set([])
            self.set = Set([])
            table_debut = self.table
            play = False
            
            while joueur.actif:
                print("la Table")
                print(self.table)
                print("Main du joueur :")
                print(joueur.main)
                action = input("Choisissez une action (poser, piocher, terminer, ajouter, retirer (pour interagir avec la table)) : ").lower()
                
                if action == "poser":
                    # Créer un set à partir de l'entrée utilisateur
                    self.set = from_input()
                    
                    # Vérification des points de début s'ils n'ont pas encore posé
                    if not joueur.debut and self.set.point() < 30:
                        print("Le joueur doit faire au moins 30 points pour commencer.")
                    elif joueur.debut or self.set.point() >= 30:
                        try:
                            joueur.pose(self.set, self.table)
                            joueur.debut = True  # Marquer que le joueur a commencé
                            play = True
                        except ValueError as e:
                            print(e)
                            
                elif action == "retirer":
                    if not joueur.debut:
                        print("Le joueur ne peut pas interagir au premier tour avant d'avoir rempli \
                la condition de départ (réaliser 30 points depuis son propre jeu)")
                    else:
                        try:
                            num_set_in_table = int(input("Le numéro du set sur la table : ")) - 1
                            tuile_retirer = from_input()  # Liste des tuiles à retirer
                
                            current_set = Set([])  # Crée un set temporaire pour les tuiles retirées
                            for t in tuile_retirer:
                                # Retire la tuile du set sur la table et l'ajoute au set temporaire
                                self.table[num_set_in_table].retr_tuile(t)
                                current_set.ajout_tuile(t)
                            
                            joueur.main.ajout_set(current_set)  # Ajoute le set temporaire à la main du joueur
                        except ValueError as e:
                            print(f"Erreur de saisie : {e}")
                        except IndexError:
                            print("Numéro de set invalide.")
                
                elif action == "ajouter":
                    if not joueur.debut:
                        print("Le joueur ne peut pas interagir au premier tour avant d'avoir rempli \
                la condition de départ (réaliser 30 points depuis son propre jeu)")
                    else:
                        try:
                            num_set_in_table = int(input("Le numéro du set sur la table : ")) - 1
                            tuile_ajouter = from_input()  # Liste des tuiles à ajouter
                
                            for t in tuile_ajouter:
                                # Ajoute la tuile au set sur la table et au set temporaire
                                self.table[num_set_in_table].ajout_tuile(t)
                                joueur.main.retr_tuile(t)
            
                        except ValueError as e:
                            print(f"Erreur de saisie : {e}")
                        except IndexError:
                            print("Numéro de set invalide.")
                                    
                elif action == "piocher":
                    try:
                        tuile_tiree = self.pioche.tirer()
                        joueur.pioche(tuile_tiree)
                        joueur.actif = False  # Terminer le tour après avoir pioché
                    except ValueError as e:
                        print(e)
                        
                elif action == "terminer":
                    if joueur.debut and self.table.check_table() and self.table.compare_Table(table_debut) and play:
                        joueur.actif = False
                        
                    else:
                        print ("le ou les sets ajouté(s) ne sont pas valide")
                
                else:
                    print("Action non reconnue. Le joueur doit choisir entre poser, piocher ou terminer.")
    
            
            
    
table = Table([])
pioche = Pioche()

set1 = Set([Tuile(10, 3),Tuile(11, 3),Tuile(0, 4),Tuile(13, 3)])
print(set1.validate())

j1 = Joueur(("gus"))
j2 = Joueur(("pat"))

partie = Partie([j1, j2], table, pioche)

partie.distribuer()

while not partie.isWinner():
    partie.tour_de_jeu()


