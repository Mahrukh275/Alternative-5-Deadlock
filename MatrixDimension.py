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
    request = [5,7,4]
             [2,3,4] #Eingabe code und Datei wird noch gemacht
    
    finish = [False]*len(ressourcentypen)

    for i in range (len(matrix)):
      if request [i][j] == 0 for j in range(len(ressourcentypen)):
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

