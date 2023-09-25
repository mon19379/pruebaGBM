archivo1 = open("output.txt","w")
archivo1.write('')

while True:
    v3 = []
    pos = []
    pos1 = []
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
        print(pos)
            
        S = int(input("Ingrese numero de sistemas de puntaje:"))

        for j in range(S): 
            v = input("Ingrese los puntos del sistema de puntaje:")
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
            ganador.append(max(v)) 
            print("ganador",ganador.index(max(v))+1)  
            empates = []
            for gan in range(len(ganador)):
                if ganador[gan] == max(v):
                    empates.append(gan+1) 
                
        print(empates)         
        
       
                





