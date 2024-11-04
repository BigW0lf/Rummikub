# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:10:58 2024

@author: Jules
"""

import sys
import jeu
from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt


class FenetrePartie(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre principale pour le démarrage de la partie
        self.setWindowTitle("Rummikub")
        self.setGeometry(100, 100, 600, 600)
        
        # Initialisation du layout principal de la fenêtre et d'une liste pour les joueurs
        layout = QVBoxLayout()
        self.liste_joueur = []  # Liste pour stocker les instances des joueurs
        
        # Création de l'interface d'accueil avec un label, un champ de texte pour le nom du joueur et des boutons
        label = QLabel("Inscris-toi à la partie")
        bouton_joueur = QPushButton("Ajouter un joueur", self) 
        bouton_start = QPushButton("Commencer la partie", self) 
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Nom du joueur")
        
        # Connexion des boutons à leurs fonctions respectives
        bouton_joueur.clicked.connect(self.ajouter_joueur)
        bouton_start.clicked.connect(self.ouvrir_fen_jeu)
        
        # Ajout des widgets dans le layout
        layout.addWidget(label, alignment=Qt.AlignTop | Qt.AlignCenter)
        layout.addWidget(self.text_input, alignment=Qt.AlignTop)
        layout.addWidget(bouton_joueur)
        layout.addWidget(bouton_start)
        
        # Définition du layout principal dans un container widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def ajouter_joueur(self):
        # Fonction pour ajouter un joueur à la liste des joueurs
        nom_joueur = self.text_input.text()
        
        if nom_joueur:  # Vérifie que le nom n'est pas vide
            self.liste_joueur.append(jeu.Joueur(nom_joueur))  # Ajoute une instance de joueur à la liste
            print(f"Joueur ajouté : {nom_joueur}")  # Affiche un message dans la console
            self.text_input.clear()  # Efface le champ de texte pour un nouveau nom
        else:
            print("Pas de nom de joueur saisi")  # Affiche un message d'erreur si le champ est vide
            
    def ouvrir_fen_jeu(self):
        # Ouvre la fenêtre de jeu avec la liste des joueurs
        self.fenetre_jeu = FenetreJeu(self.liste_joueur)
        self.close()  # Ferme la fenêtre d'ajout de joueurs
        self.fenetre_jeu.show()  # Affiche la fenêtre de jeu


class FenetreJeu(QMainWindow):
    def __init__(self, liste_joueur):
        super().__init__()
        
        # Configuration de la fenêtre de jeu
        self.setWindowTitle("Jeu Rummikub")
        self.setGeometry(150, 150, 800, 600)
        
        # Création du layout principal en grille pour la disposition des sections
        primp_layout = QGridLayout()
        
        # Layout pour les informations du jeu
        info_layout = QHBoxLayout()
        self.label_tour = QLabel("Bienvenue au jeu Rummikub!")
        self.bt_distrib = QPushButton("Distribuer pour commencer")           
        info_layout.addWidget(self.label_tour)
        info_layout.addWidget(self.bt_distrib)
        
        # Layout pour afficher la table de jeu
        table_layout = QHBoxLayout()
        self.table_label = QLabel("La table")
        table_layout.addWidget(self.table_label)
        
        # Layout pour afficher les sets des joueurs
        set_layout = QHBoxLayout()
        self.set_label = QLabel("Votre set")
        set_layout.addWidget(self.set_label)
        
        # Layout pour afficher la main d'un joueur
        main_layout = QHBoxLayout()
        self.main_label = QLabel("Votre main")
        main_layout.addWidget(self.main_label)
        
        # Placement des sections dans le layout principal
        primp_layout.addLayout(info_layout, 0, 0)
        primp_layout.addLayout(set_layout, 1, 0)
        primp_layout.addLayout(main_layout, 2, 0)
        
        # Définition du layout principal dans un container widget
        container = QWidget()
        container.setLayout(primp_layout)
        self.setCentralWidget(container)
        
    def add_Wtuile(self, area, tuile):
        # Méthode pour ajouter des tuiles au jeu, pas encore implémentée ici
        area.update  # À compléter pour mettre à jour la zone de jeu
        
    def commencer_partie(self):
        # Initialisation de la partie en distribuant les tuiles et en démarrant les tours
        table = jeu.Table([])  # Crée une nouvelle table de jeu
        pioche = jeu.Pioche()  # Crée une nouvelle pioche de tuiles
        partie = jeu.Partie(self.liste_joueur, table, pioche)  # Initialise la partie avec les joueurs, la table et la pioche
        partie.distribuer()  # Distribue les tuiles aux joueurs
        
        # Boucle pour gérer les tours jusqu'à ce qu'il y ait un gagnant
        while not partie.isWinner():
            partie.tour_de_jeu(pioche, table)  # Exécute un tour de jeu pour chaque joueur


# Initialisation de l'application et lancement de la fenêtre principale
app = QApplication(sys.argv)
fenetre = FenetrePartie()
fenetre.show()
sys.exit(app.exec_())
