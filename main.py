
#██████╗░██╗░█████╗░███╗░░░███╗░█████╗░███╗░░██╗██████╗░░██████╗████████╗░█████╗░██╗░░░░░██╗░░██╗███████╗██████╗░
#██╔══██╗██║██╔══██╗████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░██╔╝██╔════╝██╔══██╗
#██║░░██║██║███████║██╔████╔██║██║░░██║██╔██╗██║██║░░██║╚█████╗░░░░██║░░░███████║██║░░░░░█████═╝░█████╗░░██████╔╝
#██║░░██║██║██╔══██║██║╚██╔╝██║██║░░██║██║╚████║██║░░██║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██╔═██╗░██╔══╝░░██╔══██╗
#██████╔╝██║██║░░██║██║░╚═╝░██║╚█████╔╝██║░╚███║██████╔╝██████╔╝░░░██║░░░██║░░██║███████╗██║░╚██╗███████╗██║░░██║
#

# Usamos las libreias de colorama para imprimir con colores para tener una visualizacion mas correcta

import colorama
from colorama import Fore
colorama.init()

#Punt 1
# Imprimir del 0 hasta el 100 y decir cuales numeros son primos
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
print ("                 Punto 1")
print ("╭━─━─━─━─━─━─━─━─━─≪✠≫━─━─━─━─━─━──━─━─━╮")
for i in range (101):
  
  Primo = True
  if i < 2:
        Primo = False
  for n in range(2, i):
    if i % n == 0: Primo = False
  # Como estamos haciendo uso de impresion por colores
  # CYAN  --> Numeros no primos
  # RED   --> Numeros Primos
  if Primo == True : 
    print (Fore.RED+f"{i}",end=" ")
  else:  print (Fore.CYAN+f"{i}", end=" ")
print (Fore.RESET+"\n╰━─━─━─━─━─━─━─━─━─≪✠≫━─━─━─━─━─━──━─━─━╯")
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


#Punt 2
# Pedir por teclado 10 numeros enteros y mostrar si estos son pares
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
print ("                 Punto 2")
print ("╭━─━─━─━─━─━─━─━─━─≪✠≫━─━─━─━─━─━──━─━─━╮")
for i in range (11):
  Valor = int(input(Fore.RESET+" Ingrese un numero entero culaquiera:  "))
  if ( Valor % 2 == 0): print (Fore.GREEN+f" El numero {Valor} es NUMERO PAR")
  else: print (Fore.RED+f" El numero {Valor} es NUMERO IMPAR")
print (Fore.RESET+"\n╰━─━─━─━─━─━─━─━─━─≪✠≫━─━─━─━─━─━──━─━─━╯")
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛