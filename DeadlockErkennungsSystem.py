import os
import argparse
import sys
import logging


def datei_überprüfung(dateipfad):
    # Überprüft, ob die Datei am angegebenen Pfad existiert
    if not os.path.isfile(dateipfad):
        raise FileNotFoundError(f"Datei existiert nicht! {dateipfad}")


def read_vector(file_path):
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
        print("Es gab einen Fehler beim Konvertieren der Werte, es können nur ganzzahlige Werte eingelesen werden.")
        raise

# except valueError

def read_matrix(file_path):
    datei_überprüfung(file_path)
    try:
       with open(file_path,'r') as file:
            # Liest auch alle Zeilen der Datei, entfernt führende und nachfolgende Leerzeichen, teilt sie in einzelne Werte und konvertiert sie in ganzen Zahlen
            matrix = [list(map(int,line.strip().split()))for line in file]
       return matrix
    except ValueError:
         print("Fehler beim Konvertieren der Werte, es können nur ganzzahlige Werte eingelesen werden.")
         raise


#Eingabe des Ressourcenvektors
def eingabe_ressourcenvektor():
 ressourcen_laenge = int(input("Geben Sie die Anzahl der Ressourcen ein: "))
 ressourcenvektor = []  #statisch
 for i in range (ressourcen_laenge):
    eingabe = int(input("Geben Sie die Ressource "+str(i+1)+" ein: "))
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
   import random

def hole_benutzereingabe_matrix(aufforderung):
 """Erhalte eine Matrix durch Benutzereingabe"""
    print(aufforderung)
    zeilen = int(input("Anzahl der Zeilen: "))
    spalten = int(input("Anzahl der Spalten: "))
    matrix = []
    for i in range(zeilen):
        zeile = list(map(int, input(f"Geben Sie Zeile {i+1} ein: ").split()))
        matrix.append(zeile)
    return matrix
def is_deadlock (ressourcentypen, belegungsmatrix, anforderungsmatrix):
    #Initialisierung von:
    work = ressourcentypen[:] #dynamisch
    finish = [False]*len(belegungsmatrix)
    steps_log = []
    # damit diese im Log aufgezeichnet werden können

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
        steps_log.append("Keinen Deadlock erkannt.")
    else:
        steps_log.append("Deadlock erkannt.")

    for step in steps_log:
        print(step)

    return steps_log

def main():
    parser = argparse.ArgumentParser(description="Datei zum Einlesen des Ressourcenvektors, Belegungsmatrix und Anforderungsmatrix.")
    parser.add_argument('-ressourcenvektor', type=str, help='Datei für Ressourcenvektor')
    parser.add_argument('-belegungsmatrix', type=str, help='Datei für Belegungsmatrix')
    parser.add_argument('-anforderungsmatrix', type=str, help='Datei für Anforderungsmatrix')
    parser.add_argument('-logdatei', type=str, help='Datei für Logdatei')
    # str, weil der Wert des Arguments als Zeichenkette behandelt wird, da ein Dateiname eine Zeichenkette ist
    args = parser.parse_args()
    # damit das Programm die Informationen versteht und verarbeiten kann

    log_entries = []
    try:
        if args.logdatei:
            logging.basicConfig(filename=args.logdatei, level=logging.INFO)
            log = logging.getLogger()
        else:
            log = None
            # erklärung fehlt

        if args.ressourcenvektor and args.belegungsmatrix and args.anforderungsmatrix:
            ressourcenvektor = read_vector(args.ressourcenvektor)
            belegungsmatrix = read_matrix(args.belegungsmatrix)
            anforderungsmatrix = read_matrix(args.anforderungsmatrix)

        else:
            ressourcenvektor = eingabe_ressourcenvektor()
            belegungsmatrix = matrix_dimension()
            anforderungsmatrix = matrix_dimension()


        # Überprüfen, ob die Dimensionen der Matrizen korrekt sind
        if len(belegungsmatrix) != len(anforderungsmatrix):
            print("Die Anzahl der Zeilen in der Belegungs- und Anforderungsmatrix muss gleich sein.")
            sys.exit(1)

        if len(belegungsmatrix[0]) != len(ressourcenvektor) or len(anforderungsmatrix[0]) != len(ressourcenvektor):
            print("Die Anzahl der Spalten in den Matrizen muss mit der Länge des Ressourcevektors übereinstimmen.")
            sys.exit(1)

        log_entries.append(f"Ressourcenvektor: {ressourcenvektor}")
        log_entries.append(f"Belegungsmatrix: {belegungsmatrix}")
        log_entries.append(f"Anforderungsmatrix: {anforderungsmatrix}")

        result = is_deadlock(ressourcenvektor, belegungsmatrix, anforderungsmatrix)
        log_entries.extend(result)
        # erklärung

        if log:
            for entry in log_entries:
                log.info(entry)

    except (FileNotFoundError, ValueError) as e:
        print("Fehlgeschlagen: ", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
    # erklärung fehlt

