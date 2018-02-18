from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
matrix1 = []

matrix2 = [
    [2,1,0],
    [1,1,0],
    [2,0,0]
]

matrix3  = [
    [1,2,3,1],
    [4,5,6,1]
]
matrix4 = [
    [1,5],
    [2,6],
    [3,7],
    [4,8]
]
'''
matrix3a = [
    [1,2],
    [1,1],
    [0,0],
    [1,1]

]
'''
#print matrix
#print matrix1

print "Printing matrix .... "
print_matrix_p(matrix3)
#print_matrix(matrix1)

print "Printing identity matrix ... "
print_matrix(ident(matrix3))

print "Printing mult matrix ...."
print_matrix(matrix_mult(matrix3, matrix4))

print "Adding edges..."
for i in range(300):
    x1=random.randint(1,500)
    y1=random.randint(1,500)
    add_edge(matrix1,250,250,0,x1,y1,0)


print "Drawing lines....."
draw_lines( matrix1, screen, color )

display(screen)
