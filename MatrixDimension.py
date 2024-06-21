def read_matrix_from_file(file_path):
    matrix = []
    try:
        with open(file_path, 'r') as file:
            #Die Datei wird im Lesemodus geöffnet ('r')
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    row = list(map(int, stripped_line.split()))
                    matrix.append(row)
    #Fehlerbehandlung
    except FileNotFoundError:
        print(f"Die Datei {file_path} wurde nicht gefunden.")
    except ValueError:
        print("Es gab einen Fehler beim Konvertieren der Werte. Stellen Sie sicher, dass alle Werte ganze Zahlen sind.")

    return matrix
    #Beispiel für die Nutzung der Funktion
file_path = "matrix.txt"
matrix = read_matrix_from_file(file_path)
print(matrix)

#Eingabe des Ressourcenvektors
ressourcen_laenge = int(input("Geben Sie die Anzahl der Ressourcen ein: "))
ressourcentypen = []
for i in range (ressourcen_laenge):
    eingabe = int(input("Geben Sie dir Ressource "+str(i+1)+" ein: "))
    ressourcentypen.append(eingabe)


def matrix_dimension():
    print("Geben Sie die Dimension der Matrix ein: ")
    zeilen = int(input("Anzahl der Zeilen: "))
    spalten = int(input("Anzahl der Spalten: "))

    print("Geben Sie die Elemente der Matrix ein: ")
    matrix = []
    for i in range(zeilen):
        zeile = []
        for j in range(spalten):
            element = input("Element [{i}][{j}]: ")
            zeile.append(element)
    matrix.append(zeile)

    return matrix

matrix = matrix_dimension()
print("Die eingegebene Matrix ist: ")
for zeile in matrix:
    print(zeile)



#Funktion zur Deadlock-Erkennung
def is_deadlock (ressourcentypen, matrix): #anforderungsmatrix fehlt noch
    #Initialisierung von:
    work = ressourcentypen[:]
    request = [
            [5,7,4],
             [2,3,4],
             [0,0,0]
        ]#Eingabe code und Datei wird noch gemacht

    finish = [False]*len(ressourcentypen)

    for i in range (len(matrix)):
      if all (request [i][j] == 0 for j in range(len(ressourcentypen))):
          finish [i] = True
      else:
          finish[i]= False

     #Index i suchen :
    for i in range (len(matrix)):
        if not finish[i] and all(request[i][j]<= work[j]for j in range(len(ressourcentypen))):
            for j in range (len(ressourcentypen)):
                work[j] += matrix[i][j]
            finish [i] = True

    if all(finish):
        print("Keinen Deadlock erkannt.")
    else:
        print("Deadlock erkannt.")


#Ausgabe der Methode
is_deadlock(ressourcentypen, matrix)