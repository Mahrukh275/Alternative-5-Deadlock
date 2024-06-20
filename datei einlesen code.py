import os
import argparse


def datei_überprüfung(dateipfad):
    # datei_überprüfung ist die Methode bzw. Argument
    # dateipfad ist das Argument, welches angenommen wird

    if os.path.isfile(dateipfad):
        parser = argparse.ArgumentParser(description="Datei zum Einlesen des Ressourcenvektors, Belegungsmatrix und Anforderungsmatrix.")
        parser.add_argument('-ressourcenvektor', type=str, help='Datei für Ressourcenvektor')
        parser.add_argument('-belegungsmatrix', type=str, help='Datei für Belegungsmatrix')
        parser.add_argument('-anforderungsmatrix', type=str, help='Datei für Anforderungsmatrix')
        # str, weil der Wert des Arguments als Zeichenkette behandelt wird, da ein Dateiname eine Zeichenkette ist
        args = parser.parse_args(['-ressourcenvektor',dateipfad, '-belegungsmatrix',dateipfad,'-anforderungsmatrix', dateipfad])
        # damit das Programm die Informationen versteht und verarbeiten kann

        ressourcenvektor = read_vector(args.ressourcenvektor)
        belegungsmatrix = read_matrix(args.belegungsmatrix)
        anforderungsmatrix = read_matrix(args.anforderungsmatrix)
        
def read_vector(filepath):
    matrix = []

    with open(filepath, 'r') as file:
    #'r' steht nur für das Lesen der Datei
        for line in file:
        #Schleife, um jede Zeile der Datei einzulesen
            line.strip().split()
            #line.strip() entfernt Leerzeichen
            matrix.append([float(num) for num in line.strip().split()])
            #float??
    return matrix

def read_matrix(filepath):
    return read_vector(filepath)

if __name__ == "__main__":
    

