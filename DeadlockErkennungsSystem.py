import os
import argparse
import sys
import logging


def datei_überprüfung(dateipfad):
    # datei_überprüfung ist die Methode bzw. Argument
    # dateipfad ist das Argument, welches angenommen wird
    if not os.path.isfile(dateipfad):
        print("Datei existiert nicht!")
        sys.exit(1)
        #sys.exit(1) dient dazu um das Programm zu beenden

def read_vector(file_path):
   datei_überprüfung(file_path)
   try:
        with open(file_path, 'r') as file:
         # 'r' steht nur für das Lesen der Datei
            vector = list(map(int, file.readline().strip().split()))
        return vector
# return vector, damit der vector zur weiterverarbeitung der deadlock Erkennung verwendet werden kann
   except ValueError:
        print("Es gab einen Fehler beim Konvertieren der Werte. Stellen Sie sicher, dass alle Werte ganze Zahlen sind.")
        sys.exit(1)

# except valueError

def read_matrix(file_path):
    datei_überprüfung(file_path)
    try:
       with open(file_path,'r') as file:
            matrix = [list(map(int,line.strip().split()))for line in file]
        # erklärung fehlt!
       return matrix
    except ValueError:
         print("Fehler beim Konvertieren der Werte. Stellen Sie sicher, dass alle Werte ganze Zahlen sind.")
         sys.exit(1)

def matrix_dimension():
        print("Geben Sie die Dimension der Matrix ein: ")
        zeilen = int(input("Anzahl der Zeilen: "))
        spalten = int(input("Anzahl der Spalten: "))

        print("Geben Sie die Elemente der Matrix ein: ")
        matrix = []
        for i in range(zeilen):
            zeile = []
            for j in range(spalten):
                element = input(f"Element [{i}][{j}]: ")
                zeile.append(element)
            matrix.append(zeile)

        return matrix

def is_deadlock (ressourcentypen, belegungsmatrix, anforderungsmatrix):
    #Initialisierung von:
    work = ressourcentypen[:]
    finish = [False]*len(ressourcentypen)

    while True:
        for i in range(len(belegungsmatrix)):
            if all(request[i][j] == 0 for j in range(len(ressourcentypen))):
                finish[i] = True
            else:
                finish[i] = False

            # Index i suchen :
        for i in range(len(matrix)):
            if not finish[i] and all(request[i][j] <= work[j] for j in range(len(ressourcentypen))):
                for j in range(len(ressourcentypen)):
                    work[j] += matrix[i][j]
                finish[i] = True

        if all(finish):
            print("Keinen Deadlock erkannt.")
        else:
            print("Deadlock erkannt.")


def main():
    parser = argparse.ArgumentParser(description="Datei zum Einlesen des Ressourcenvektors, Belegungsmatrix und Anforderungsmatrix.")
    parser.add_argument('-ressourcenvektor', type=str, help='Datei für Ressourcenvektor')
    parser.add_argument('-belegungsmatrix', type=str, help='Datei für Belegungsmatrix')
    parser.add_argument('-anforderungsmatrix', type=str, help='Datei für Anforderungsmatrix')
    parser.add_argument('-logdatei', type=str, help='Datei für Logdatei')
    # str, weil der Wert des Arguments als Zeichenkette behandelt wird, da ein Dateiname eine Zeichenkette ist
    args = parser.parse_args()
    # damit das Programm die Informationen versteht und verarbeiten kann

    if args.logdatei:
        logging.basicConfig(filename=args.logdatei, level = logging.INFO)
        log = logging.getLogger()
    else:
        log = none
    # erklärung fehlt


    if args.ressourcenvektor:
       ressourcenvektor =read_vector(args.ressourcenvektor)

    else:
       resssourcenvektor =is_deadlock()

    if args.belegungsmatrix:
        belegungsmatrix = read_matrix(args.belegungsmatrix)

    else:

    if args.anforderungsmatrix:
        anforderungsmatrix = anforderungsmatrix_read(args.anforderungsmatrix)
    else:

if __name__ == "__main__":
    main()
    # erklärung fehlt