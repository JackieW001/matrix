from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
matrix1 = [
    [1,1,0],
    [2,1,0],
    [1,2,0]
]
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

draw_lines( matrix, screen, color )
#display(screen)
