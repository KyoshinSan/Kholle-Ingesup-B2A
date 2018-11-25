#!/usr/bin/python36
# -*- coding: utf-8 -*-

# Nom : DINH_Jonathan_kholle_1.py
# Description : Rendu kholle 1
# Date : 24/11/2018
# Auteur : DINH Jonathan

##### IMPORTS #####

import argparse
import csv
import os

##### VARIABLES #####

# argparse permet de lire les arguments de la commande

parser = argparse.ArgumentParser()
parser.add_argument('-l', action='store_true', help='Affiche le contenu de la liste')
parser.add_argument('-a', nargs='+', type=int, help='Ajouter les ITEMS dans la liste', metavar='ITEM')
parser.add_argument('-c', action='store_true', help='Supprime tous les elements de la liste')
parser.add_argument('-s', choices=['max', 'min', 'moy', 'sum'], help='Afficher la valeur max/min/de la moyenne/de la somme')
parser.add_argument('-t', choices=['asc', 'desc'], help="Trier dans l'ordre croissant/decroissant")
args = parser.parse_args()

fichier_csv = './liste_entiers.csv'


##### FONCTIONS #####

# fonction qui permet de lire les nombres dans le fichier csv

def lire_fichier_csv(fichier):
    nombres = []
    with open(fichier_csv, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            nombres = row
    return nombres


# fonction qui permet d ecrire dans le fichier csv

def ecrire_fichier_csv(fichier, data):
    with open(fichier, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# fonction qui efface le contenu du fichier csv

def effacer_fichier_csv(fichier):
    with open(fichier, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow('')


# fonction qui retourne le maximum

def maximum(liste_nombre):
    nombres = []
    for nombre in liste_nombre:
        nombres.append(int(nombre))
    return max(nombres)


# fonction qui retourne le minimum

def minimum(liste_nombre):
    nombres = []
    for nombre in liste_nombre:
        nombres.append(int(nombre))
    return min(nombres)


# fonction qui retourne la somme

def somme(liste_nombre):
    nombres = []
    for nombre in liste_nombre:
        nombres.append(int(nombre))
    return sum(nombres)


# fonction qui retourne la moyenne

def moyenne(liste_nombre):
    moyenne = somme(liste_nombre) / len(liste_nombre)
    return moyenne


# fonction qui tri dans l ordre croissant

def tri_croissant(liste_nombre):
    nombres = []
    for nombre in liste_nombre:
        nombres.append(int(nombre))
    nombres.sort()
    ecrire_fichier_csv(fichier_csv, nombres)


# fonction qui tri dans l ordre decroissant

def tri_decroissant(liste_nombre):
    nombres = []
    for nombre in liste_nombre:
        nombres.append(int(nombre))
    nombres.sort(reverse=True)
    ecrire_fichier_csv(fichier_csv, nombres)


# fonction qui verifie si le fichier csv existe

def csv_is_exist():
    if not os.path.isfile(fichier_csv):
        with open(fichier_csv, 'w') as f:
            f.write('')


##### SCRIPT #####

csv_is_exist()

if args.l:
    print(lire_fichier_csv(fichier_csv))

elif args.a:
    liste_nombre = lire_fichier_csv(fichier_csv)
    for nombre in args.a:
        liste_nombre.append(nombre)
    ecrire_fichier_csv(fichier_csv, liste_nombre)
    print('Nombre ajoute !')

elif args.c:
    effacer_fichier_csv(fichier_csv)
    print('Contenu effacer !')

elif args.s:
    if args.s == 'max':
        try:
            print('Le maximum : ' + str(maximum(lire_fichier_csv(fichier_csv))))
        except ValueError:
            print('Ajouter des nombres a la liste !')

    elif args.s == 'min':
        try:
            print('Le minimum : ' + str(minimum(lire_fichier_csv(fichier_csv))))
        except ValueError:
            print('Ajouter des nombres a la liste !')

    elif args.s == 'moy':
        try:
            print('La moyenne : ' + str(moyenne(lire_fichier_csv(fichier_csv))))
        except:
            print('Ajouter des nombres a la liste !')

    elif args.s == 'sum':
        if len(lire_fichier_csv(fichier_csv)) > 0:
            print('La somme : ' + str(somme(lire_fichier_csv(fichier_csv))))
        else:
            print('Ajouter des nombres a la liste !')

elif args.t:
    if args.t == 'asc':
        tri_croissant(lire_fichier_csv(fichier_csv))
        print('Tri par ordre croissant effectuer !')

    elif args.t == 'desc':
        tri_decroissant(lire_fichier_csv(fichier_csv))
        print('Tri par ordre decroissant effectuer !')

