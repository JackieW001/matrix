from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
color = [ 255, 255, 255 ]
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
print_matrix_p(ident(matrix3))

print "Printing mult matrix ...."
print_matrix_p(matrix3)
print "times"
print_matrix_p(matrix4)
print_matrix_p(matrix_mult(matrix3, matrix4))

print "Adding edges..."
for i in range(100):
    x0=random.randint(1,500)
    y0=random.randint(1,500)
    for j in range(15):
        x1=random.randint(-5,5)+x0
        y1=random.randint(-5,5)+y0
        add_edge(matrix1,x0,y0,0,x1,y1,0)


print "Drawing lines....."
draw_lines( matrix1, screen, color )

display(screen)
save_extension(screen, 'snowflake.png')
