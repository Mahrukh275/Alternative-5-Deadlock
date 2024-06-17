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
