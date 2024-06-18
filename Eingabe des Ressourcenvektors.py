#Eingabe des Ressourcenvektors
ressoucen_laenge = int(input("Geben Sie die Anzahl der Ressourcen ein: "))

ressourcentypen = []
for i in range(ressoucen_laenge):
    eingabe= int(input("Geben Sie die Ressource "+str(i+1)+" ein"))
    ressourcentypen.append(eingabe)