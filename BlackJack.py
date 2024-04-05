#Juego : Black Jack (21 en Latinoamérica)
# Autores : Juan Alanís, Daniel Servín y Jesús Melesio 
# Fecha de publicación : 29 de noviembre de 2023
# Licencia : MIT 


#import numpy as np 
from numpy import random 
#Importamos el módulo random, el cual necesitamos para seleccionar aleatoriamente las cartas 

#Creamos dos clases, que son como moldes, uno para el dealer y otro para los jugadores. Las variables adentro son los atributos 
class dealer: 
    def __init__(dealer,dealerPuntos): 

        dealer.dealerPuntos = dealerPuntos

class jugadorNormal:
    def __init__(jugador,nombre,puntos, NumeroJugador):
        jugador.nombre = nombre 
        jugador.puntos = puntos 
        jugador.NumeroJugador = NumeroJugador


#arrVacio = [] 
#jugadooor.puntos 
#for p in range(1,NumeroJugadores+1):
    #arrVacio.append(jugadooor.puntos)


while True:
    print("Bienvenido a Black Jack\n")
    print("Menú\n")
    print("""
    1. Presione 1 si desea iniciar una partida nueva
    2. Presione 2 si no desea continuar jugando
    3. Presione 3 si desea consultar el manual del juego""")
    #Este es el menú, muestra las opciones que el jugador puede seleccionar 
    
    Decision = input()

    #Si el jugador decide iniciar una partida, debe presionar 1, entonces el programa lo detecta y entra en esta condición. 
    if Decision == '1':
        print("Por favor, introduce el número de jugadores. El dealer es la computadora\n") 
        NumeroJugadores = int(input())
        #Le solicitamos al usuario que ingrese el número de jugadores sin considerar al dealer.
        
        while NumeroJugadores > 5:
          
            print("El límite de jugadores, sin contar al dealer, es 5. Introduce un número válido\n")
            NumeroJugadores = int(input())
            
                    

        if NumeroJugadores <= 5:
            
            #Este ciclo nos permite instanciar objetos, en este caso, crearle un usuario a cada jugador sin considerar al dealer 
            puntosJugadores = []
            for i in range(1,NumeroJugadores+1):
                
                print("Introduce tu nombre, jugador", i)
                nombre = input()
                jugadooor = jugadorNormal(nombre,None,i)
                i = jugadooor.NumeroJugador
                print("El jugador", jugadooor.NumeroJugador, "es", jugadooor.nombre,"\n")

                
                #El método choice nos permite seleccionar aleatoriamente un número del arreglo mostrado, como sacar una bola en un sorteo
                d = random.choice([1,2,3,4,5,6,7,8,9,10,11])
                # Este número seleccionado representa una carta. Verificamos si la carta extraída es un As
                if d == 1 or d == 11:
                        print(jugadooor.nombre,"te ha salido un As, su valor es ",d, "¿Deseas conservar su valor?SI/NO\n")
                        #El jugador tiene el derecho de decidir si el As vale 1 u 11 según le salga el número 
                        Respuesta = input()
                        if Respuesta.upper() == 'NO':
                            if d == 11:
                                d = 1 
                                print("Tu carta ha sido cambiada por ",d,"\n")
                            elif d == 1:
                                d = 11
                                print("Tu carta ha sido cambiada por ",d,"\n")

                #Si la carta no es un As, entonces se le muestra al jugador cuál es el valor de su carta
                print("Para", jugadooor.nombre, "su primera carta es ", d,"\n")

                #Se le da al jugador otra carta, de igual modo, seleccionada aleatoriamente. 
                for j in range(1,2):
                    n = random.choice([1,2,3,4,5,6,7,8,9,10,11])
                    #Aquí se hace la misma prueba e implementación para el jugador 2 sobre si le sale un As
                    if n == 1 or n == 11:
                        print(jugadooor.nombre, "te ha salido un As, su valor es ",n, "¿Deseas conservar su valor?SI/NO\n")
                        Respuesta2 = input()
                        if Respuesta2.upper() == 'NO':
                            if n == 11:
                                n = 1 
                                print("Tu carta ha sido cambiada por ",n,"\n")
                            elif n == 1:
                                n = 11
                                print("Tu carta ha sido cambiada por ",n,"\n")

                    print("Para", jugadooor.nombre, "su segunda carta es ", n,"\n")
                
                jugadooor.puntos = n + d 
                #Verificamos si la puntuación del jugador coincide con 21, si es así, entonces ha hecho un black jack y se acaba la partida
                if jugadooor.puntos == 21:
                    print("¡Felicidades, jugador",jugadooor.NumeroJugador,  " haz hecho un Black Jack! Ganó", jugadooor.nombre,"\n")
                    puntosJugadores.append(jugadooor.puntos)
                    #print(puntosJugadores)
                    print("---------------------------------------------")
                    break 
                elif jugadooor.puntos > 21:
                    
                    print("Tu puntuación excede 21. No puedes seguir sacando cartas. Estás fuera")
                    puntosJugadores.append(jugadooor.puntos)
                    print(puntosJugadores)
                    print("---------------------------------------------")
                
                elif jugadooor.puntos <21:
                #Si la puntuación excede el número 21, el jugador queda fuera de la partida, sin posibilidad de entrar hasta que se inicie una nueva partida
                
                    print(jugadooor.nombre, "tu puntuación te permite seguir sacando cartas ¿deseas pedir otra carta?SI/NO","\n") 
                    #Aquí se le pregunta al jugador si desea pedir otra carta, si este accede, entonces se ejecuta el siguiente bloque de código 
                    PedirCarta = input()
                    
                    if PedirCarta.upper() == 'SI':
                        #Ciclo que va sacando cartas al azar
                        while jugadooor.puntos < 21:
                            m = random.choice([1,2,3,4,5,6,7,8,9,10,11])
                            print("Tu nueva carta es", m)
                            #Para verificar si la nueva carta es un As. Como se aprecia, el As es una carta no trivial en este juego 
                            if m == 1 or m == 11:
                                    print(jugadooor.nombre, "te ha salido un As, su valor es ",m, "¿Deseas conservar su valor?SI/NO\n")
                                    Respuesta3 = input()  
                                    #Se le pregunta al jugador qué valor desea que adopte su As, o bien, si desea conservar el valor por default
                                    if Respuesta3.upper() == 'NO':
                                        if m == 11:
                                            m = 1 
                                            print("Tu carta ha sido cambiada por ",m,"\n")
                                            
                                        elif m == 1:
                                            m = 11
                                            print("Tu carta ha sido cambiada por ",m,"\n")
                                            
                            jugadooor.puntos = jugadooor.puntos + m
                            if jugadooor.puntos > 21: 
                                print("Tu puntuación excede 21.No puedes seguir sacando cartas. Estás fuera")
                                puntosJugadores.append(jugadooor.puntos)
                                #print(puntosJugadores)
                                break 
                            
                            print(jugadooor.nombre, "tu puntuación actual es", jugadooor.puntos)
                            print(jugadooor.nombre, ",tu puntuación te permite seguir sacando cartas ¿deseas pedir otra carta?SI/NO","\n")

                            PedirCarta = input()
                            if PedirCarta.upper() == 'NO':
                                print(jugadooor.nombre, "ha decidido no sacar más cartas")
                                puntosJugadores.append(jugadooor.puntos)
                                #print(puntosJugadores)
                                break 

                        print("Los puntos acumulados de ", jugadooor.nombre, "son ", jugadooor.puntos,"\n")
                        print("---------------------------------------------")
                            
                    elif PedirCarta.upper() == 'NO':
                    
                        print("Los puntos acumulados de ", jugadooor.nombre, "son", jugadooor.puntos,"\n")
                        puntosJugadores.append(jugadooor.puntos)
                        #print(puntosJugadores)
                        print("---------------------------------------------")

            #Aunque el array inicialmente se llame arrVacio, notamos que se ha ido rellenando, mencionamos esto para evitar confusiones
            print("Las puntuaciones de los jugadores son: ", puntosJugadores)
            if max(puntosJugadores) < 21:
                print("La puntuación más alta fue: ", max(puntosJugadores))
            elif max(puntosJugadores) >= 21:
                print("Ningún jugador distinto al dealer gana la ronda. ")
            print("\n")
            print("---------------------------------------------")
            print("\n")
            print("Para el dealer")
                #Aquí finaliza el turno del jugador, se calcula su puntuación, incluso si sacó otra carta o más, esta también se contempla
            
            CartaVolteada = random.choice([1,2,3,4,5,6,7,8,9,10,11])
            CartaVisible = random.choice([1,2,3,4,5,6,7,8,9,10,11])
                #Una de las cartas extraídas no debe ser volteada o mostrada hasta que finalice la partida
                #dealerDecision = None
                #Esta variable está declarada así debido a que si al dealer le sale un As, este pueda escoger entre cambiar el valor o dejarlo igual, es una manera de automatizar el proceso, mediante el azar


                #Sección para el dealer. Para fines prácticos, el dealer es la computadora. 
                #El dealer recibe dos cartas al azar de manera obligatoria, al igual que los otros jugadores. Además, la suma de los valores de estas cartas no debe exceder el número 17, si esto no pasa, está obligado a sacar una tercer carta, luego decide si seguir sacando cartas mientras la puntuación sea menor a 21
            
                #Instanciamos el objeto dealer, con sus respectivos atributos 
            #Con esto se soluciona el problema de la creación del objeto dealer, que ocurrió el 30/11/2023
            dealer = dealer(None)
            #Calculamos la puntuación actual del dealer
            dealer.dealerPuntos = CartaVolteada + CartaVisible

            if dealer.dealerPuntos == 21:
                print("Felicidades, haz hecho un black jack. Ganó el dealer\n")
                break 
 
                #Le mostramos al dealer sus cartas
            print("La carta 1 del dealer es ", CartaVisible)

                #Para continuar jugando si su puntuación no es 21 (si no ha hecho un black jack), la puntuación actual (la suma de las dos cartas extraídas) no debe exceder 17 puntos
            if dealer.dealerPuntos <17: 
                    
                if CartaVolteada == 1 or CartaVolteada == 11:
                        print("Dealer, la carta oculta es un As, su valor es ",CartaVolteada, "¿Deseas conservar su valor?SI/NO\n")
                        dealerDecision = random.choice(['SI','NO'])
                        print("La decisión del dealer es: ",dealerDecision)
                        if dealerDecision == 'NO':
                            if CartaVolteada == 11:
                                CartaVolteada = 1 
                                        
                            elif CartaVolteada == 1:
                                CartaVolteada = 11
                                        
                elif CartaVisible == 1 or CartaVisible == 11:
                            print("Dealer, te ha salido un As, su valor es ",CartaVisible, "¿Deseas conservar su valor?SI/NO\n")     
                            dealerDecision = random.choice(['SI','NO'])
                            print("La decisión del dealer es: ",dealerDecision)   
                            if dealerDecision == 'NO':
                                if CartaVisible == 11:
                                    CartaVisible = 1 
                                        
                                elif CartaVisible == 1:
                                    CartaVisible = 11

                #Verificamos si la carta obligatoria es un As o no
                z = random.choice([1,2,3,4,5,6,7,8,9,10,11])
                print("La nueva carta obligatoria del dealer es ", z)
                if z == 1 or z == 11:
                                print("Dealer, te ha salido un As, su valor es ",z , "¿deseas conservar su valor?SI/NO\n")
                                dealerDecision = random.choice(['SI','NO'])
                                print("La decisión del dealer es: ",dealerDecision)
                                #Se le pregunta al dealer qué valor desea que adopte su As, o bien, si desea conservar el valor por default
                                if dealerDecision == 'NO':
                                    if z == 11:
                                        z = 1
                                        print("El As del dealer ahora vale ",z,"\n") 
                                        
                                    elif z == 1:
                                        z = 11
                                        print("El As del dealer ahora vale ",z,"\n") 

                #Calculamos la puntuación actual del dealer
                dealer.dealerPuntos = CartaVisible + CartaVolteada + z
                print("Dealer, tu puntuación actual es: ", dealer.dealerPuntos,"\n")
                

                if dealer.dealerPuntos < 21:
                    print("Tu puntuación actual te permite seguir sacando cartas, ¿deseas seguir sacando cartas?\n")
                    pedirCartaDealer = random.choice(['SI','NO'])

                    if pedirCartaDealer == 'SI':
                        #Ciclo que va sacando cartas al azar
                        print("La respuesta del dealer es: ",pedirCartaDealer,"\n")
                        while dealer.dealerPuntos < 21 and pedirCartaDealer!='NO':
                            k = random.choice([1,2,3,4,5,6,7,8,9,10,11])
                            print("El dealer ha sacado una nueva carta, esta es ", k)
                            #Para verificar si la nueva carta es un As. 
                            if k == 1 or k == 11:
                                    print("Dealer, te ha salido un As, su valor es ",k, "¿Deseas conservar su valor?SI/NO\n")
                                    dealerCambiarAs = random.choice(['SI','NO'])  
                                    print(dealerCambiarAs)
                                    #Se le pregunta al dealer qué valor desea que adopte su As, o bien, si desea conservar el valor por default
                                    if dealerCambiarAs == 'NO':
                                        if k == 11:
                                            k = 1
                                            print("El As del dealer ahora vale ",k,"\n") 
                                            
                                        elif k == 1:
                                            k = 11
                                            print("El As del dealer ahora vale ",k,"\n") 
                            #Notamos que la puntuación del dealer ya no es la misma que la de la línea 211
                            dealer.dealerPuntos = dealer.dealerPuntos + k   
                              
                            #Si el anterior bloque de código no detecta un As, procedemos a calcular la puntuación del dealer 
                        

                            print("Dealer, ¿deseas seguir sacando cartas?\n")
                            pedirCartaDealer = random.choice(['SI','NO'])
                            print("La respuesta del dealer es: ", pedirCartaDealer, "\n")
                            
                        
                        print("La puntuación del dealer ha excedido los 21. No puede seguir sacando cartas")
                        print("La carta oculta del dealer, la que mantuvo volteada, es", CartaVolteada,"\n")
                        print("La puntuación final del dealer es ", dealer.dealerPuntos,"\n")
                        #En este bloque de código se hacen las comparaciones entre las puntuaciones de los jugadores y el dealer, se determina quién ganó en caso de no haber salido algún Black Jack
                        if max(puntosJugadores) < dealer.dealerPuntos and dealer.dealerPuntos < 21:
                            print("La puntuación ganadora es: ", dealer.dealerPuntos)  
                        elif max(puntosJugadores) > dealer.dealerPuntos and dealer.dealerPuntos >= 21:
                            print("Partida muerta. Nadie ganó")
                        elif max(puntosJugadores) > dealer.dealerPuntos and dealer.dealerPuntos < 21: 
                            print("La puntuación ganadora es: ", max(puntosJugadores))
                        elif max(puntosJugadores) < dealer.dealerPuntos and dealer.dealerPuntos >=21:
                            print("La puntuación ganadora es:", max(puntosJugadores))
                        break 
                    
                        #print("---------------------------------------------")
                

                        
                    elif pedirCartaDealer == 'NO':
                        print("La respuesta del dealer es: ",pedirCartaDealer,"\n")
                        print("El dealer ha decidido no sacar más cartas. La carta oculta del dealer, la que mantuvo volteada, es", CartaVolteada,"\n")
                        dealer.dealerPuntos = CartaVolteada + CartaVisible + z
                        print("La puntuación final del dealer es ", dealer.dealerPuntos,"\n")
                        #En este bloque de código se hacen las comparaciones entre las puntuaciones de los jugadores y el dealer, se determina quién ganó en caso de no haber salido algún Black Jack
                        if max(puntosJugadores) < dealer.dealerPuntos and dealer.dealerPuntos < 21:
                            print("La puntuación ganadora es: ", dealer.dealerPuntos)  
                        elif max(puntosJugadores) > dealer.dealerPuntos and dealer.dealerPuntos >= 21:
                            print("Partida muerta. Nadie ganó")
                        elif max(puntosJugadores) > dealer.dealerPuntos and dealer.dealerPuntos < 21: 
                            print("La puntuación ganadora es: ", max(puntosJugadores))
                        elif max(puntosJugadores) < dealer.dealerPuntos and dealer.dealerPuntos >=21:
                            print("La puntuación ganadora es:", max(puntosJugadores))
                        break 
                    
                    

                elif dealer.dealerPuntos >= 21:
                    print("La puntuación del dealer es ", dealer.dealerPuntos)
                    print("La puntuación del dealer igualó o excedió 21 puntos, por lo que no puede sacar más cartas. Su carta volteada es",CartaVolteada,"\n")
                    #En este bloque de código se hacen las comparaciones entre las puntuaciones de los jugadores y el dealer, se determina quién ganó en caso de no haber salido algún Black Jack
                    if max(puntosJugadores) < dealer.dealerPuntos and dealer.dealerPuntos < 21:
                        print("La puntuación ganadora es: ", dealer.dealerPuntos)  
                    elif max(puntosJugadores) > dealer.dealerPuntos and dealer.dealerPuntos >= 21:
                        print("Partida muerta. Nadie ganó")
                    elif max(puntosJugadores) > dealer.dealerPuntos and dealer.dealerPuntos < 21: 
                        print("La puntuación ganadora es: ", max(puntosJugadores))
                    elif max(puntosJugadores) < dealer.dealerPuntos and dealer.dealerPuntos >=21:
                        print("La puntuación ganadora es:", max(puntosJugadores))
                    
                    break   
            else:
                print("La puntuación del dealer es ", dealer.dealerPuntos)
                print("La puntuación del dealer igualó o excedió 17 puntos, por lo que no puede sacar más cartas. Su carta oculta es",CartaVolteada,"\n")
                #En este bloque de código se hacen las comparaciones entre las puntuaciones de los jugadores y el dealer, se determina quién ganó en caso de no haber salido algún Black Jack
                if max(puntosJugadores) < dealer.dealerPuntos and dealer.dealerPuntos < 21:
                    print("La puntuación ganadora es: ", dealer.dealerPuntos)  
                elif max(puntosJugadores) > dealer.dealerPuntos and dealer.dealerPuntos >= 21:
                    print("Partida muerta. Nadie ganó")
                elif max(puntosJugadores) > dealer.dealerPuntos and dealer.dealerPuntos < 21: 
                    print("La puntuación ganadora es: ", max(puntosJugadores))
                elif max(puntosJugadores) < dealer.dealerPuntos and dealer.dealerPuntos >=21:
                    print("La puntuación ganadora es:", max(puntosJugadores))
                
            
    elif Decision == '2':
        print("Gracias por jugar. Vuelva pronto")
        #Para NO iniciar una partida o para no seguir jugando 
        break 

    elif Decision == '3':
        print("En breve se le mostrará un manual\n")
        #Utilizamos la función open para abrir en modo lectura el manual, el cual es un archivo de texto
        AbrirManual = open("Manual.txt","rt")
        #Mostramos el texto en pantalla 
        print(AbrirManual.read())
        #Siempre es importante cerrar el archivo de texto 
        AbrirManual.close()
          



