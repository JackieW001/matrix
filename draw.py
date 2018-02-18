from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    if (len(matrix)%2 == 1):
        add_point(matrix,0,0,0)
    for i in xrange(0,len(matrix),2):
        j = i+1
        draw_line(matrix[i][0],
                  matrix[i][1],
                  matrix[j][0],
                  matrix[j][1],
                  screen,
                  color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    point1 = [ x0, y0, z0 ]
    point2 = [ x1, y1, z1 ]
    matrix.append(point1)
    matrix.append(point2)
    return matrix

def add_point( matrix, x, y, z=0 ):
    point = [x,y,z]
    matrix.append(point)
    return matrix



def draw_line( x0, y0, x1, y1, screen, color ):
    
    if (x0 < x1):
        x = x0
        y = y0
    else:
        x = x1
        y = y1
        x1 = x0
        y1 = y0

    A = y1-y
    B = -(x1-x)

    # Slope = 0
    if (B == 0):
        if (y1 < y):
            temp = y
            y = y1
            y1 = temp
        while (y<=y1):
            plot(screen, color, x, y)
            y += 1
        return
    else:
        slope = (A*1.0)/-B
        
    #Octant I
    if( slope <= 1 and slope >= 0):
        d = (2*A) + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += (2*B)
            x += 1
            d += (2*A)

    #Octant II
    elif( slope > 1 ):
        d = A + (B*2)
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += (2*A)
            y += 1
            d += (2*B)

    #Octant VIII
    elif( slope >= -1 and slope < 0):
        d = (2*A)-B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= (2*B)
            x += 1
            d += (2*A)

    #Octant VII
    elif( slope < -1):
        d = A - (2*B)
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += (2*A)
            y -= 1
            d -= (2*B)
    '''
    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1
#end draw_line
    '''
