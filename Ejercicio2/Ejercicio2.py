archivo1 = open("output.txt","w")
archivo1.write('')

while True:
    v3 = []
    v4 = []
    pos = []
    pos1 = []
    pos2=[]
    pos3=[]
    puntaje = []
    lista = []
    val = 0
    G = 0
    P = 0
    entrada1 = 0
    S = 0
    ganador = []
    v = 0
    entrada1 = input("Ingresa el numero de Grand Prix y de Pilotos:")
    
    v1,v2 = entrada1.split()
    G = int(v1)
    P = int(v2)

    if G == 0 and P == 0:
        break
    
    else:

        
        for i in range(G):    
            pos.append(input("Ingrese el resultado de la carrera separado por espacios:"))
            pos1 = pos[i].split()
            for j in pos1:
                pos2.append(int(j))
            pos3.append(pos2)
            
        S = int(input("Ingrese numero de sistemas de puntaje:"))

        for j in range(S): 
            v3=[]
            v = input("Ingrese los puntos del sistema de puntaje:")
            v2 = v.split()
            for i in v2:
                v3.append(int(i))
            v4.append(v3)
            puntaje.append(str(P)+ " " + v)
            
        
        archivo = open("Output.txt","a")
        archivo.write("INPUTS\n")
        archivo.write(entrada1 + "\n")
    
        print(entrada1)
        
        for k in range (G):
            print(pos[k])
            archivo.write(pos[k] + "\n")
        print(S)
        archivo.write(str(S)+ "\n")

        for x in range(S):
            print(puntaje[x])
            archivo.write(puntaje[x]+ "\n") 
            archivo.write("Piloto ganador:" + str(pos3[0][v4[x].index(max(v4[x]))])+"\n")
            print("Piloto ganador:",pos3[0][v4[x].index(max(v4[x]))] )
            





