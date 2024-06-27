import os
import argparse
import sys
import logging


def datei_überprüfung(dateipfad):
    # Überprüft, ob die Datei am angegebenen Pfad existiert
    # dateipfad ist das Argument, welches angenommen wird
    if not os.path.isfile(dateipfad):
        print("Datei existiert nicht!")
        sys.exit(1)
        #sys.exit(1) Beendet das Programm mit Statuscode 1

def read_vector(file_path):
    #Liest einen Vektor aus einer Datei
   datei_überprüfung(file_path)
   try:
        with open(file_path, 'r') as file:
         # 'r' steht nur für das Lesen der Datei
         # Öffnet die Datei im Lesemodus
            vector = list(map(int, file.readline().strip().split()))
         # Liest die erste Zeile der Datei, entfernt führende und nachfolgende Leerzeichen,
         # teilt sie in einzelne Werte und konvertiert sie in ganze Zahlen
        return vector
# return vector, damit der vector zur weiterverarbeitung der deadlock Erkennung verwendet werden kann
   except ValueError:
       # Fehlerbehandlung für den Fall, dass die Konvertierung in ganze Zahlen fehlschlägt
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


#Eingabe des Ressourcenvektors
def eingabe_ressourcenvektor():
 ressourcen_laenge = int(input("Geben Sie die Anzahl der Ressourcen ein: "))
 ressourcenvektor = []  #statisch
 for i in range (ressourcen_laenge):
    eingabe = int(input("Geben Sie dir Ressource "+str(i+1)+" ein: "))
    ressourcenvektor.append(eingabe)

 return ressourcenvektor

def matrix_dimension():
        print("Geben Sie die Dimension der Matrix ein: ")
        zeilen = int(input("Anzahl der Zeilen: "))
        spalten = int(input("Anzahl der Spalten: "))

        print("Geben Sie die Elemente der Matrix ein: ")
        matrix = []
        for i in range(zeilen):
            zeile = []
            for j in range(spalten):
                element = int(input(f"Element [{i}][{j}]: "))
                zeile.append(element)
            matrix.append(zeile)

        return matrix

def is_deadlock (ressourcentypen, belegungsmatrix, anforderungsmatrix):
    #Initialisierung von:
    work = ressourcentypen[:] #dynamisch
    finish = [False]*len(belegungsmatrix)

    for i in range(len(belegungsmatrix)):
            if all(anforderungsmatrix[i][j] == 0 for j in range(len(ressourcentypen))):
                finish[i] = True

    while True:
        progress = False
          # Index i suchen
        for i in range(len(belegungsmatrix)):
            if not finish[i] and all(anforderungsmatrix[i][j] <= work[j] for j in range(len(ressourcentypen))):
                for j in range(len(ressourcentypen)):
                    work[j] += belegungsmatrix[i][j]
                finish[i] = True
                progress = True
                break

        if not progress:
            break

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
        logging.basicConfig(filename=args.logdatei, level=logging.INFO)
        log = logging.getLogger()
    else:
        log = none
        # erklärung fehlt

        if args.ressourcenvektor:
            if args.ressourcenvektor and args.anforderungsmatrix and args.belegungsmatrix:
                ressourcenvektor = read_vector(args.ressourcenvektor)
                belegungsmatrix = read_matrix(args.belegungsmatrix)
                anforderungsmatrix = read_matrix(args.anforderungsmatrix)

            else:
                resssourcenvektor = eingabe_ressourcenvektor()
                belegungsmatrix = matrix_dimension()
                anforderungsmatrix = matrix_dimension()

        is_deadlock(resssourcenvektor, belegungsmatrix, anforderungsmatrix)

    if __name__ == "__main__":
        main()
        # erklärung fehlt

    if args.logdatei:
        logging.basicConfig(filename=args.logdatei, level = logging.INFO)
        log = logging.getLogger()
    else:
        log = none
    # erklärung fehlt


    if args.ressourcenvektor and args.anforderungsmatrix and args.belegungsmatrix:
       ressourcenvektor =read_vector(args.ressourcenvektor)
       belegungsmatrix = read_matrix(args.belegungsmatrix)
       anforderungsmatrix = read_matrix(args.anforderungsmatrix)

    else:
       resssourcenvektor = eingabe_ressourcenvektor()
       belegungsmatrix = matrix_dimension()
       anforderungsmatrix = matrix_dimension()


    is_deadlock(resssourcenvektor,belegungsmatrix,anforderungsmatrix)
if __name__ == "__main__":
    main()
    # erklärung fehlt

