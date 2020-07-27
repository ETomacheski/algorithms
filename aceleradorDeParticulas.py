from math import floor
distancia = int(input())
distancia = distancia - 3 

voltas = floor(distancia/8)

distanciatotal = voltas*8

if(distanciatotal +5 <= distancia or distanciatotal +3 > distancia and distancia >=8):
  print(3)
  
elif (distanciatotal +4 <= distancia):
  print(2)
  
else:
  print(1)
