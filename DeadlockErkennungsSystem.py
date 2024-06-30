import os
import argparse
import sys
import logging
import random


def datei_überprüfung(dateipfad):
    # Überprüft, ob die Datei am angegebenen Pfad existiert
    if not os.path.isfile(dateipfad):
        print (f"Datei existiert nicht! {dateipfad}")
        sys.exit(1)


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
        sys.exit(1)

# except valueError

def read_matrix(file_path):
    datei_überprüfung(file_path)
    try:
       with open(file_path,'r') as file:
            # Liest auch alle Zeilen der Datei, entfernt führende und nachfolgende Leerzeichen, teilt sie in einzelne Werte und konvertiert sie in ganzen Zahlen
            matrix = [list(map(int,line.strip().split()))for line in file]

       if any(len(row) != len(matrix[0]) for row in matrix):
           print("Die Spaltenzahl in allen Zeilen der Matrizen muss übereinstimmen..")
           sys.exit(1)

       return matrix
    except ValueError:
         print("Fehler beim Konvertieren der Werte, es können nur ganzzahlige Werte eingelesen werden.")
         sys.exit(1)


#Eingabe des Ressourcenvektors
def eingabe_ressourcenvektor():
 ressourcen_laenge = int(input("Geben Sie die Anzahl der Ressourcen ein: "))
 ressourcenvektor = []  #statisch
 for i in range (ressourcen_laenge):
    eingabe = int(input("Geben Sie die Ressource "+str(i+1)+" ein: "))
    ressourcenvektor.append(eingabe)
 return ressourcenvektor

def matrix_dimension(matrix_name):
        print(f"Geben Sie die Dimension der {matrix_name} ein: ")
        zeilen = int(input("Anzahl der Zeilen: "))
        spalten = int(input("Anzahl der Spalten: "))

        print(f"Geben Sie die Elemente der {matrix_name} ein: ")
        matrix = []
        for i in range(zeilen):
            zeile = []
            for j in range(spalten):
                element = int(input(f"Element [{i}][{j}]: "))
                zeile.append(element)
            matrix.append(zeile)

        return matrix


# Funktion zur Überprüfung auf Deadlock
def is_deadlock (ressourcentypen, belegungsmatrix, anforderungsmatrix, noninteractive=False):
    #Initialisierung von:
    work = ressourcentypen[:] #dynamisch
    finish = [False]*len(belegungsmatrix) #Liste für den Abschlusszustand der Prozesse
    steps_log = []

    while True:
        progress = False
        available_processes = []

          # Index i suchen
        for i in range(len(belegungsmatrix)):
            if not finish[i] and all(anforderungsmatrix[i][j] <= work[j] for j in range(len(ressourcentypen))):
                available_processes.append(i)
                
        if not available_processes:
            break

        if noninteractive:
             # Wenn der nicht-interaktive Modus aktiviert ist, wählt einen zufälligen Prozess aus den verfügbaren Prozessen aus
            next_process = random.choice(available_processes)
            print(f"Zufällig ausgewählter Prozess: {next_process}")
        else:
            # Wenn der interaktive Modus aktiviert ist, fördert den Benutzer auf, einen Prozess auszuwählen
            print("Mehrere Prozesse können ausgeführt werden:")
            for process in available_processes:
                print(f"Prozess {process}")
            next_process = int(input("Welcher Prozess soll als nächstes ausgeführt werden? "))


        for j in range(len(ressourcentypen)):
            work[j] += belegungsmatrix[next_process][j]

        finish[next_process] = True
        steps_log.append(f"Ausgeführt: Prozess {next_process}")

    if not any(finish):

        # Markieret den ausgewählten Prozess als abgeschlossen und füge ihn zum Schritt-Log hinzu
        finish[next_process] = True
        steps_log.append(f"Ausgeführt: Prozess {next_process}")

    # Überprüft, ob alle Prozesse abgeschlossen sind

    if all(finish):

        return False, steps_log  # Kein Deadlock
    else:
        return True, steps_log  # Deadlock
        
    # wird in steps_log aufgenommen, damit dies in die Logdatei aufgenommen werden kann
# Hauptfunktion
def main():
    parser = argparse.ArgumentParser(description="Datei zum Einlesen des Ressourcenvektors, Belegungsmatrix und Anforderungsmatrix.(Optional eine Logdatei)")
    parser.add_argument('-ressourcenvektor', type=str, help='Datei für Ressourcenvektor')
    parser.add_argument('-belegungsmatrix', type=str, help='Datei für Belegungsmatrix')
    parser.add_argument('-anforderungsmatrix', type=str, help='Datei für Anforderungsmatrix')
    parser.add_argument('-logdatei', type=str, help='Datei für Logdatei')
    parser.add_argument('-noninteractive', action='store_true', help='Führt den Simulator im nicht-interaktiven Modus aus')
    # str, weil der Wert des Arguments als Zeichenkette behandelt wird, da ein Dateiname eine Zeichenkette ist
    args = parser.parse_args()
    # damit das Programm die Informationen versteht und verarbeiten kann


    if args.logdatei:
        logging.basicConfig(filename=args.logdatei, level=logging.INFO)
        # falls der Benutzer eine Logdatei erstellen möchte, werden die Einträge protokolliert
        logger = logging.getLogger()
    else:
        logger = None

    steps_log = []
    # Schritte des Programms werden aufgezeichnet

    if args.ressourcenvektor and args.belegungsmatrix and args.anforderungsmatrix:
        ressourcenvektor = read_vector(args.ressourcenvektor)
        belegungsmatrix = read_matrix(args.belegungsmatrix)
        anforderungsmatrix = read_matrix(args.anforderungsmatrix)

    else:
        ressourcenvektor = eingabe_ressourcenvektor()
        belegungsmatrix = matrix_dimension("Belegungsmatrix")
        anforderungsmatrix = matrix_dimension("Anforderungsmatrix")


       # Überprüfen, ob die Dimensionen der Matrizen korrekt sind
    if len(belegungsmatrix) != len(anforderungsmatrix):
        print("Die Anzahl der Zeilen in der Belegungs- und Anforderungsmatrix muss gleich sein.")
        sys.exit(1)

    if len(belegungsmatrix[0]) != len(ressourcenvektor) or len(anforderungsmatrix[0]) != len(ressourcenvektor):
        print("Die Anzahl der Spalten in den Matrizen muss mit der Länge des Ressourcevektors übereinstimmen.")
        sys.exit(1)

    result, deadlock_log = is_deadlock(ressourcenvektor, belegungsmatrix, anforderungsmatrix,args.noninteractive)
    if args.noninteractive:
         # Wenn der nicht-interaktive Modus aktiviert ist, gibt die Ausführungsinformationen ohne Benutzerinteraktion aus
        print(f"Ausführung im nicht-interaktiven Modus:")
        for entry in deadlock_log:
            print(entry) # Gibt jeden Eintrag im deadlock_log auf der Konsole aus
            if logger:
                logger.info(entry) # Schreibt jeden Eintrag im deadlock_log in die Logdatei, falls ein logger definiert ist
    else:
        # Wenn der interaktive Modus aktiviert ist, gibt es  die Ausführungsinformationen mit Benutzerinteraktion aus
        for entry in deadlock_log:
            print(entry) # Gibt jeden Eintrag im deadlock_log auf der Konsole aus
            if logger:
                logger.info(entry) # Schreibt jeden Eintrag im deadlock_log in die Logdatei, falls ein logger definiert ist
    # deadlock_log protokolliert während der Deadlock Überprüfung
    if deadlock_log is None:
        print("Fehler: is_deadlock() hat keinen deadlock_log zurückgegeben.")
        sys.exit(1)

    steps_log.extend(deadlock_log)
    # Zusammenführung beider Logs für die vollständige Aufzeichnung des Programms

    if result:
        print("Deadlock erkannt")
    else:
        print ("Kein Deadlock erkannt")

    steps_log = []
    steps_log.append(f"Ressourcenvektor: {ressourcenvektor}")
    steps_log.append(f"Belegungsmatrix: {belegungsmatrix}")
    steps_log.append(f"Anforderungsmatrix: {anforderungsmatrix}")
    # Werte werden in die Logdatei geschrieben

    if logger:
        for entry in steps_log:
            logger.info(entry)
            # Ergebnis wird hiermit aufgenommen


if __name__ == "__main__":
    main()

