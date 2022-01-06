import os
from math import sin, cos, pi
 
round = lambda a: int(a*100)/100
def rotation(point, theta):
    x = point[0]
    y = point[1]
    xprime = x * cos(theta) - (y * sin(theta))
    yprime = y * cos(theta) + x * sin(theta)
    return [round(xprime), round(yprime)]
 
#works lmao
directions = [
   [2, 2, 1],
   [2, 2, 2],
   [2, 2, 3],
   [2, 2, 4],
   [2, 2, 5],
   [2, 2, 6],
   [10, 5, 7],
   [12, 5 , 8],
   [4, 1, 9],
   [4, 1, 10],
   [4, 1, 11],
   [4, 1, 12],
   [4, 1, 13],
   [4, 1, 14],
   [4, 1, 15],
   [4, 1, 16],
   [4, 1, 17],
   [4, 1, 18],
   [4, 1, 19],
   [4, 1, 20],
   [4, 1, 21],
   [4, 1, 22],
   [4, 1, 23],
   [4, 1, 24],
   [4, 1, 25],
   [4, 1, 26],
   [4, 1, 27],
   [4, 1, 28],
   [4, 1, 29],
   [4, 1, 30],
   [4, 1, 31],
   [4, 1, 32],
   [4, 1, 33],
   [4, 1, 34],
   [4, 1, 35],
   [4, 1, 36],
   [4, 1, 37],
   [4, 1, 38],
   [4, 1, 39],
   [4, 1, 40],
   [4, 1, 41],
   [4, 1, 42],
   [4, 1, 43],
   [4, 1, 44],
   [4, 1, 45],
   [4, 1, 46],
   [4, 1, 47],
   [4, 1, 48],
   [4, 1, 49],
   [4, 1, 50],
   [2, 1, 51],
   [2, 1, 52],
   [2, 1, 53],
   [1, 1, 54],
]
 
def sword(width = 80,  height = 55):
    angle = 0
    while 1:
        k = ""
        step = 0
        for z in range(height):
           e = 0
           one = ""
           if directions[step][2] == z:
               point1 = [directions[step][0], directions[step][1]]
               point2 = [-directions[step][0], -directions[step][1]]
               newpoint1 = rotation(point1, angle)
               newpoint2 = rotation(point2, angle)
               difference = abs(newpoint1[0] - newpoint2[0])
               while e <= difference:
                   one = one + "1"
                   e += 1
               if step < len(directions) - 1:
                   step += 1
           k = k + one.center(width, " ")   
        print(k)
        angle += pi/288
        if angle == 2*pi:
            angle = 0
        clearing = "clear" #whatever clears your command line, i think it is cls for windows
        os.system(clearing)
        
      
  
try:
    sword()
    #sword(columns, rows)
except KeyboardInterrupt:
   print("no sword :(")
 
 
 
 
 



