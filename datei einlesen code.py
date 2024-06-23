import os
import argparse
import sys


def datei_überprüfung(dateipfad):
    # datei_überprüfung ist die Methode bzw. Argument
    # dateipfad ist das Argument, welches angenommen wird
    if not os.path.isfile(dateipfad):
        print("Datei existiert nicht!")
        sys.exit(1)
        #sys.exit(1) dient dazu um das Programm zu beenden

def read_vector(file_path):
   datei_überprüfung(file_path)
    #try....
        with open(filepath, 'r') as file:
         # 'r' steht nur für das Lesen der Datei
            vector = list(map(int, file.readline().strip().split()))
        return vector
# return vector, damit der vector zur weiterverarbeitung der deadlock Erkennung verwendet werden kann

# except valueError

def read_matrix(file_path):
    datei_überprüfung(file_path)
    with open(file_path,'r') as file:
        matrix = [list(map(int,line.strip().split()))for line in file]
        # erklärung fehlt!
    return matrix

def main():
    parser = argparse.ArgumentParser(description="Datei zum Einlesen des Ressourcenvektors, Belegungsmatrix und Anforderungsmatrix.")
    parser.add_argument('-ressourcenvektor', type=str, help='Datei für Ressourcenvektor')
    parser.add_argument('-belegungsmatrix', type=str, help='Datei für Belegungsmatrix')
    parser.add_argument('-anforderungsmatrix', type=str, help='Datei für Anforderungsmatrix')
    # str, weil der Wert des Arguments als Zeichenkette behandelt wird, da ein Dateiname eine Zeichenkette ist
    args = parser.parse_args()
    # damit das Programm die Informationen versteht und verarbeiten kann

    if args.ressourcenvektor:
       ressourcenvektor =read_vector(args.ressourcenvektor)

    else:
       # manuelle eingabe

    if args.belegungsmatrix:
        belegungsmatrix = read_matrix(args.belegungsmatrix)

    else:

    if args.anforderungsmatrix:
        anforderungsmatrix = anforderungsmatrix_read(args.anforderungsmatrix)
    else:

if __name__ == "__main__":
    main()
    # erklärung fehlt

