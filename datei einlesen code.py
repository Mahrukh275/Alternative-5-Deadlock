import os
import argparse


def datei_überprüfung(dateipfad):
    # datei_überprüfung ist die Methode bzw. Argument
    # dateipfad ist das Argument, welches angenommen wird

    if os.path.isfile(dateipfad):
        parser = argparse.ArgumentParser(
            description="Datei zum Einlesen des Ressourcenvektors, Belegungsmatrix und Anforderungsmatrix.")
        parser.add_argument('-ressourcenvektor', type=str, help='Datei für Ressourcenvektor')
        parser.add_argument('-belegungsmatrix', type=str, help='Datei für Belegungsmatrix')
        parser.add_argument('-anforderungsmatrix', type=str, help='Datei für Anforderungsmatrix')
        # str, weil der Wert des Arguments als Zeichenkette behandelt wird, da ein Dateiname eine Zeichenkette ist
        args = parser.parse_args()
        # damit das Programm die Informationen versteht und verarbeiten kann

        ressourcenvektor = read_vector(args.ressourcenvektor)
        belegungsmatrix = read_matrix(args.belegungsmatrix)
        anforderungsmatrix = read_matrix(args.anforderungsmatrix)
